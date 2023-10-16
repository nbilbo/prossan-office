import tkinter as tk
from abc import ABC

import ttkbootstrap as ttk

from app import constants
from app.ui.components import Table
from app.utils import images


class ManagerPage(ABC, ttk.Frame):
    """
    Base class for managing registers within the application.

    This class provides a base structure for managing various registers.
    """

    def __init__(self, master: tk.Misc) -> None:
        """
        Initialize the NavBar widget.

        :param master: The parent widget to which this widget will be attached.
        """
        super().__init__(master)
        self.search_img = images.image_tk(constants.ICONS_DIR / 'search.png', (32, 32))
        self.add_img = images.image_tk(constants.ICONS_DIR / 'add-person.png', (32, 32))
        self.details_img = images.image_tk(constants.ICONS_DIR / 'details-person.png', (32, 32))
        self.pdf_img = images.image_tk(constants.ICONS_DIR / 'pdf.png', (32, 32))
        self.delete_img = images.image_tk(constants.ICONS_DIR / 'delete-person.png', (32, 32))

        self.title_label = ttk.Label(self)
        self.title_label.config(text='Titulo')
        self.title_label.config(anchor=ttk.CENTER)
        self.title_label.pack(side=ttk.TOP, fill=ttk.X)

        search_container = ttk.Frame(self)
        search_container.pack(side=ttk.TOP, fill=ttk.X, pady=10)

        self.search_entry = ttk.Entry(search_container)
        self.search_entry.config(width=1)
        self.search_entry.pack(side=ttk.LEFT, fill=ttk.BOTH, expand=ttk.YES)

        self.search_button = ttk.Button(search_container)
        self.search_button.config(text='Pesquisar')
        self.search_button.config(image=self.search_img, compound=tk.RIGHT)
        self.search_button.config(cursor='hand2')
        self.search_button.pack(side=ttk.LEFT, fill=ttk.BOTH)

        self.table = Table(self)
        self.table.set_columns(('ID', 'Nome', 'CPF', 'RG'))
        self.table.pack(side=ttk.TOP, fill=ttk.BOTH, expand=ttk.YES)

        actions_container = ttk.Frame(self)
        actions_container.pack(side=ttk.TOP, fill=ttk.X, pady=10)

        self.create_button = ttk.Button(actions_container)
        self.create_button.config(text='Adicionar')
        self.create_button.config(width=1)
        self.create_button.config(image=self.add_img, compound=tk.RIGHT)
        self.create_button.config(cursor='hand2')
        self.create_button.pack(side=ttk.LEFT, fill=ttk.BOTH, expand=ttk.YES, padx=10)

        self.details_button = ttk.Button(actions_container)
        self.details_button.config(text='Detalhes')
        self.details_button.config(width=1)
        self.details_button.config(image=self.details_img, compound=tk.RIGHT)
        self.details_button.config(cursor='hand2')
        self.details_button.pack(side=ttk.LEFT, fill=ttk.BOTH, expand=ttk.YES)

        self.pdf_button = ttk.Button(actions_container)
        self.pdf_button.config(text='PDF')
        self.pdf_button.config(width=1)
        self.pdf_button.config(image=self.pdf_img, compound=tk.RIGHT)
        self.pdf_button.config(cursor='hand2')
        self.pdf_button.pack(side=ttk.LEFT, fill=ttk.BOTH, expand=ttk.YES, padx=10)

        self.delete_button = ttk.Button(actions_container)
        self.delete_button.config(text='Deletar')
        self.delete_button.config(width=1)
        self.delete_button.config(image=self.delete_img, compound=tk.RIGHT)
        self.delete_button.config(cursor='hand2')
        self.delete_button.pack(side=ttk.LEFT, fill=ttk.BOTH, expand=ttk.YES)

        # noinspection PyArgumentList
        self.search_button.config(bootstyle='default-link')

        # noinspection PyArgumentList
        self.create_button.config(bootstyle='default-link')

        # noinspection PyArgumentList
        self.details_button.config(bootstyle='default-link')

        # noinspection PyArgumentList
        self.pdf_button.config(bootstyle='default-link')

        # noinspection PyArgumentList
        self.delete_button.config(bootstyle='default-link')
