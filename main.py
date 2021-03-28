from mainwindow import Mainwindow
from decryptor import Decryptor
from encryptor import Encryptor
from tkinter import *

mainwindow = Mainwindow()

#key = b'1234'
#enc = Encryptor(key)
#enc.encrypt_file("cat.jpg")
#dec = Decryptor(key)
#dec.decrypt_file("cat.jpg")

mainwindow.loop()
