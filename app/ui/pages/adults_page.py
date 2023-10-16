import tkinter as tk

from app.ui.pages import ManagerPage


class AdultsPage(ManagerPage):
    """
    Page for managing adults' information.

    This page is responsible for managing and displaying information about adults registers.
    """

    def __init__(self, master: tk.Misc) -> None:
        super().__init__(master)
        self.title_label.config(text='Adultos')
