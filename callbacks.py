from tkinter import messagebox
from tkinter import filedialog


class Callbacks:
    """A class to manage callbacks from a buttons"""

    def __init__(self):
        pass

    def encrypt_button(self):
        # TODO
        response = messagebox.askyesno("Enrypt", "Are you sure?")
        pass

    def decrypt_button(self):
        # TODO
        response = messagebox.askyesno("Decrypt", "Are you sure?")
        pass

    def open_file(self):
        # init open file dialog
        self.filename = filedialog.askopenfilename(
            initialdir="", title="Select a file")
        pass
