from settings import Settings
from tkinter import *
from PIL import Image, ImageTk
from callbacks import Callbacks


class Mainwindow:
    """A class to represent main window of a program"""

    def __init__(self):
        """Init the window"""
        self.root = Tk()

        self.settings = Settings()
        self.root.title(self.settings.title)
        self.root.geometry(self.settings.geometry)
        self._set_background()
        self.root.iconbitmap(self.settings.icon)

        self.callbacks = Callbacks()

        # init entry text
        self.password = Entry(
            self.root, show="*", width=self.settings.entry_width, border=self.settings.entry_border)
        self.password.grid(row=1, column=1)
        # self.password.pack()

        # init buttons
        self.encryptionButton = Button(self.root, text="Encrypt",
                                       padx=self.settings.padx, pady=self.settings.pady, command=self.callbacks.encrypt_button)
        self.encryptionButton.grid(row=2, column=0)
       # self.encryptionButton.pack()
        self.decryptionButton = Button(self.root, text="Decrypt",
                                       padx=self.settings.padx, pady=self.settings.pady, command=self.callbacks.decrypt_button)
        self.decryptionButton.grid(row=2, column=2)
       # self.decryptionButton.pack()

    def _set_background(self):
        """set background image"""
        self.bg_image = Image.open(self.settings.bg_image)
        self.bg_image_tk = ImageTk.PhotoImage(self.bg_image)
        self.bg_label = Label(self.root, image=self.bg_image_tk)
        self.bg_label.grid(row=0, column=0, columnspan=3, rowspan=4)

    def loop(self):
        self.root.mainloop()
