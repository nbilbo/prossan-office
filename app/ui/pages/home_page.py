import tkinter as tk

import ttkbootstrap as ttk


class HomePage(ttk.Frame):
    """
    Represents the home page of the application.

    This page serves as the main entry point of the application and may contain informations.
    """

    def __init__(self, master: tk.Misc) -> None:
        super().__init__(master)
