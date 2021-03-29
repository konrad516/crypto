from settings import Settings
from tkinter import *
from PIL import Image, ImageTk
from callbacks import Callbacks
from tkinter import filedialog


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
        self.pass_label = Label(self.root, text="Password: ")
        self.pass_label.grid(row=1, column=2)
        self.password = Entry(
            self.root, show="*", width=self.settings.entry_width, border=self.settings.entry_border)
        self.password.grid(row=1, column=3)

        # init entry local path
        self.path_text = Label(self.root, text="Local path: ")
        self.path_text.grid(row=2, column=2)
        self.path_label = Label(self.root, text="please click below to load file",
                                width=self.settings.entry_width, border=self.settings.entry_border)
        self.path_label.grid(row=2, column=3)

        self.__buttons_init()

    def __buttons_init(self):
        """funcion to manage buttons"""
        self.encryptionButton = Button(self.root, text="Encrypt",
                                       padx=self.settings.padx, pady=self.settings.pady, command=lambda: self.callbacks.encrypt_button(self.password.get(), self.path))
        self.encryptionButton.grid(row=3, column=2)

        self.decryptionButton = Button(self.root, text="Decrypt",
                                       padx=self.settings.padx, pady=self.settings.pady, command=lambda: self.callbacks.decrypt_button(self.password.get(), self.path))
        self.decryptionButton.grid(row=3, column=4)

        self.openButton = Button(self.root, text="Load file",
                                 padx=self.settings.padx, pady=self.settings.pady, command=self.open_file)
        self.openButton.grid(row=3, column=3)

    def _set_background(self):
        """set background image"""
        self.bg_image = Image.open(self.settings.bg_image)
        self.bg_image_tk = ImageTk.PhotoImage(self.bg_image)
        self.bg_label = Label(self.root, image=self.bg_image_tk)
        self.bg_label.grid(
            row=0, column=0, columnspan=self.settings.columnspan, rowspan=self.settings.rowspan)

    def open_file(self):
        # init open file dialog
        self.path = filedialog.askopenfilename(
            initialdir="/", title="Select a file")
        self.path_label = Label(self.root, text=self.path,
                                width=self.settings.entry_width, border=self.settings.entry_border)
        self.path_label.grid(row=2, column=3)

    def loop(self):
        self.root.mainloop()
