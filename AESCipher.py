import hashlib
import base64
from Crypto import Random
from Crypto.Cipher import AES
import aes

class AESCipher(object):
    """Class for AES encryption"""

    def __init__(self, key):
        """Init objecy with a key"""
        self.key = hashlib.sha256(key).digest()

    def encrypt(self, text):
        """Encrypts 'text' text with a self.key using AES algorithm"""
        # add padd
        text = self._pad(text)
        # choose random initialization vector (IV)
        iv = Random.new().read(AES.block_size)
        # create AES CBC mode cipher
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        # encrypt
        return base64.b64encode(iv + cipher.encrypt(text))


    def encrypt2(self, text):
        """Encrypts 'text' text with a expanded key using implemented AES algorithm"""
        # add padd
        text = self._pad(text)
        key=aes.expand_key(self.key)
        # choose random initialization vector (IV)
        iv = Random.new().read(AES.block_size)
        # create AES CBC mode cipher
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        # encrypt
        return base64.b64encode(iv + aes.encrypt(key,iv,text))


    def decrypt(self, text):
        """Decrypts encrypted 'text' with a self.key using AES algorithm"""
        text = base64.b64decode(text)
        iv = text[:AES.block_size]
        # create AES CBC mode cipher
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        # decrypt
        plaintext = cipher.decrypt(text[AES.block_size:])
        return plaintext.rstrip(b"\0")


    def decrypt2(self, text):
        """Decrypts encrypted 'text' with a expanded key using implemented AES algorithm"""
        text = base64.b64decode(text)
        iv = text[:AES.block_size]
        key=aes.expand_key(self.key)
        plaintext = aes.decrypt(key,iv,text[AES.block_size:])
        return plaintext.rstrip(b"\0")


    def _pad(self, s):
        """Adds a number bytes for str to be multiple of 128"""
        return s + b"\0" * (AES.block_size - len(s) % AES.block_size)


    @staticmethod
    def _unpad(str):
        """Remove all added characters"""
        return str[:-ord(str[len(str)-1:])]
