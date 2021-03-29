from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from decryptor import Decryptor
from encryptor import Encryptor


class Callbacks:
    """A class to manage callbacks from a buttons"""

    def __init__(self):
        self.key = None
        pass

    def encrypt_button(self, passwd, filename):
        response = messagebox.askyesno("Enrypt", "Are you sure?")
        if(response):
            self.key = passwd.encode('UTF-8')
            enc = Encryptor(self.key)
            enc.encrypt_file(filename)
        pass

    def decrypt_button(self, passwd, filename):
        response = messagebox.askyesno("Decrypt", "Are you sure?")
        if(response):
            self.key = passwd.encode('UTF-8')
            dec = Decryptor(self.key)
            dec.decrypt_file(filename)
        pass

        pass
