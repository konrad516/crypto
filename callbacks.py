from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import filedialog
from decryptor import Decryptor
from encryptor import Encryptor

class Callbacks:
    """A class to manage callbacks from a buttons"""
    

    def __init__(self):
        pass

    def encrypt_button(self,passwd):
        response = messagebox.askyesno("Enrypt", "Are you sure?")
        key = passwd.encode('UTF-8')
        enc = Encryptor(key)
        enc.encrypt_file(self.filename)
        pass

    def decrypt_button(self,passwd):
        response = messagebox.askyesno("Decrypt", "Are you sure?")
        key = passwd.encode('UTF-8')
        dec = Decryptor(key)
        dec.decrypt_file(self.filename)
        pass

    def open_file(self):
        # init open file dialog
        self.filename = filedialog.askopenfilename(
            initialdir="/", title="Select a file", filetype=(("all files", "*.*"), ("jpg files", "*.jpg")))
        pass
