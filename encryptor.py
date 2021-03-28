import AESCipher


class Encryptor:
    def __init__(self, key):
        self.key = key

    def encrypt_file(self, file_name):
        aes = AESCipher(self.key)
        with open(file_name, 'rb') as file:
            text = file.read()
            enc = aes.encrypt(text)
        with open(file_name + ".encrypted", 'wb') as file:
            file.wirte(enc)
