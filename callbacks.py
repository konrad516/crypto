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
        response = False
        if (filename == ""):
            messagebox.showerror("Error", "Please select a file!")
        elif(passwd == ""):
            messagebox.showerror("Error", "Please enter a password!")
        else:
            response = messagebox.askyesno("Enrypt", "Are you sure?")
        if(response):
            self.key = passwd.encode('UTF-8')
            enc = Encryptor(self.key)
            enc.encrypt_file(filename)
            messagebox.showinfo("Succes", "Encryption successful")
        pass

    def decrypt_button(self, passwd, filename):
        response = False
        if (filename == ""):
            messagebox.showerror("Error", "Please select a file!")
        elif(passwd == ""):
            messagebox.showerror("Error", "Please enter a password!")
        else:
            response = messagebox.askyesno("Decrypt", "Are you sure?")
        if(response):
            self.key = passwd.encode('UTF-8')
            dec = Decryptor(self.key)
            dec.decrypt_file(filename)
            messagebox.showinfo("Succes", "Decryption successful")
        pass
