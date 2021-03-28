from mainwindow import Mainwindow
from decryptor import Decryptor
from encryptor import Encryptor
from tkinter import *
from PIL import Image, ImageTk


mainwindow = Mainwindow()

key = b'1234'
enc = Encryptor(key)
enc.encrypt_file("ccat.jpg")
dec = Decryptor(key)
dec.decrypt_file("cat.jpg.encrypted")

mainwindow.loop()
