import hashlib
import base64
from Crypto import Random
from Crypto.Cipher import AES


class AESCipher(object):
    """Class for AES encryption"""

    def __init__(self, key):
        """Init objecy with a key"""
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, text):
        """Encrypts 'text' text with a self.key using AES algorithm"""
        # add padd
        text = self._pad(text)
        # choose random initialization vector (IV)
        iv = Random.new().read(AES.block_size)
        # create AES CBC mode cipher
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        # encrypt
        return base64.b64encode(iv + cipher.encrypt(text.encode()))

    def decrypt(self, text):
        """Decrypts encrypted 'text' with a self.key using AES algorithm"""
        text = base64.b64decode(text)
        iv = text[:AES.block_size]
        # create AES CBC mode cipher
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        # decrypt
        return self._unpad(cipher.decrypt(text[AES.block_size:])).decode('utf-8')

    def _pad(self, str):
        """Adds a number bytes for s to be multiple of 128"""
        return str + (AES.block_size - len(str) % AES.block_size) * chr(AES.block_size - len(str) % AES.block_size)

    @staticmethod
    def _unpad(str):
        """Remove all added characters"""
        return str[:-ord(str[len(str)-1:])]
