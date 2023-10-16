import tkinter as tk
from abc import ABC

import ttkbootstrap as ttk
from ttkbootstrap.scrolled import ScrolledFrame


class BaseForm(ABC, ttk.Toplevel):
    """
    A base class for creating forms in a tkinter application.

    This class provides a base structure for creating forms within a tkinter application.
    It includes a scrollable container and a header title.
    """

    def __init__(self, master: tk.Misc) -> None:
        """
        Initialize the BaseForm.

        :param master: The parent widget.
        """
        super().__init__(master=master)
        self.geometry('900x500+0+0')

        self.container = ScrolledFrame(self)
        self.container.config(padding=20)
        self.container.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES)

        self.header_title = ttk.Label(self.container)
        self.header_title.config(anchor=tk.CENTER)
        self.header_title.pack(side=tk.TOP, fill=tk.X, pady=10)
