#!/usr/bin/env python
# -*- coding: utf-8 -*-

def convert_key(s):
    return [ord(c) for c in s]

def KSA(key):
    keylength = len(key)

    S = range(256)

    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % keylength]) % 256
        S[i], S[j] = S[j], S[i]
    return S

def PRGA(S):
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]

        K = S[(S[i] + S[j]) % 256]
        yield K

def RC4(key):
    S = KSA(key)
    return PRGA(S)


def encr(msg,key):

    key = convert_key(key)
    
    keystream = RC4(key)
    cript = ""
    for c in msg:
        cript+= "%02X" % (ord(c) ^ keystream.next())

    print("Dado gerado > " + cript.decode("hex"))

    dcr(cript,key)


def dcr(msg,key):

    keystream = RC4(key)
    decript = ""
    for c in msg.decode("hex"):
        decript+="%02X" % (ord(c) ^ keystream.next())
    print("Dado original > "+decript.decode("hex"))


msg = "A945CA494757258A015216A74FCAC0CFBF9D362635E3C23193FFA37E3D9FB98B94836A9FD6773E87AB0B62AD71D7E551CCC5029E4A227A7DC86030BC5397073BD992AC0D290B320E548F857EE81944F6AD16B49D3B9A724E96F2AA64084793EB875DAEE5E3BB216E42583AF99829F22BB454EC518F8B8DBA3D01519E37E67D0C8B3C5F95BFAC77DD04E923B75E4688CBA32F6E2EA23E00706C06B8C536C85007D481988EF0A7F84894C74FA8824BFE9018F112AAABFCA38E13F1F8B103550B9321CEB4E01071C2A70B64C7E62560DD6EAEFE75318CB3D76088D032988D07EDC157F91716F4F39551AE4D9BF7612D26503C89F033963DDA3619E1"

key = '204'
