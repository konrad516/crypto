from aescipher import AESCipher


class Decryptor:
    def __init__(self, key):
        self.key = key

    def decrypt_file(self, file_name):
        aes = AESCipher(self.key)
        with open(file_name, 'rb') as file:
            text = file.read()
        dec = aes.decrypt(text)
        with open(file_name, 'wb') as file:
            file.write(dec)
