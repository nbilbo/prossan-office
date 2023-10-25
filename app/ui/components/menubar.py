import tkinter as tk

import ttkbootstrap as ttk


class Menubar(ttk.Menu):
    """
    A custom menu bar for the application.
    """

    def __init__(self, master: tk.Misc) -> None:
        """
        Initialize a new instance of the Menubar.

        :param master: The parent widget to which this menu bar is attached.
        """
        super().__init__(master=master)
        self.file_menu = ttk.Menu(self)
        self.help_menu = ttk.Menu(self)

        self.add_cascade(label='Arquivo', menu=self.file_menu)
        self.add_cascade(label='Ajuda', menu=self.help_menu)
