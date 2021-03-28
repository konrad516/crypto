from mainwindow import Mainwindow
from decryptor import Decryptor
from encryptor import Encryptor
from tkinter import *
from PIL import Image, ImageTk


mainwindow = Mainwindow()

key = b'1234'
enc = Encryptor(key)
enc.encrypt_file("crypto\\text.txt")
dec = Decryptor(key)
dec.decrypt_file("crypto/text.txt.encrypted")

mainwindow.loop()
