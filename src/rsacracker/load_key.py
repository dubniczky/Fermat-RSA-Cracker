from base64 import b64decode

from Crypto.PublicKey import RSA


def public(key):
    key = b64decode(key)
    pub = RSA.importKey(key)
    return (pub.e, pub.n)
