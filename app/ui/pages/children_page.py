import tkinter as tk

from app.ui.pages import ManagerPage


class ChildrenPage(ManagerPage):
    """
    Page for managing children's information.

    This page is responsible for managing and displaying information about children registers.
    """

    def __init__(self, master: tk.Misc) -> None:
        super().__init__(master)
        self.title_label.config(text='Crianças e adolecentes')
