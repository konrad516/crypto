class Settings:
    """A class to store all settings for a program"""

    def __init__(self):
        """Init the program settings"""

        # define screen settings
        self.title = "Image Encryption"
        self.geometry = "640x409"
        self.bg_image = "background.jpg"
        self.icon = "icon.ico"
        self.columnspan = 5
        self.rowspan = 6

        # define entry text settings
        self.entry_width = 60
        self.entry_border = 5

        # define buttons settings
        self.padx = 25
        self.pady = 5

        # define AES settings
        self.BS = 16
