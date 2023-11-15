import tkinter as tk
from typing import Tuple

import ttkbootstrap as ttk

from app import constants
from app.utils import images


class NavBar(ttk.Frame):
    """
    A custom widget for a navigation bar.

    This widget provides navigation buttons for different sections of the application.
    """

    def __init__(self, master: tk.Misc) -> None:
        """
        Initialize the NavBar widget.

        :param master: The parent widget to which this widget will be attached.
        """
        super().__init__(master)
        self.index_img = images.image_tk(constants.ICONS_DIR / 'index.png', (52, 52))
        self.children_img = images.image_tk(constants.ICONS_DIR / 'children.png', (52, 52))
        self.adults_img = images.image_tk(constants.ICONS_DIR / 'adults.png', (52, 52))

        self.default_bootstyle = 'default-link'
        self.focus_bootstyle = 'primary'

        self.home_button = ttk.Button(self)
        self.home_button.config(text='Inicio')
        self.home_button.config(image=self.index_img, compound=tk.TOP)
        self.home_button.config(cursor='hand2')
        self.home_button.pack(side=ttk.TOP, fill=ttk.BOTH, expand=ttk.YES)

        self.children_button = ttk.Button(self)
        self.children_button.config(text='Crianças e adolencentes')
        self.children_button.config(image=self.children_img, compound=tk.TOP)
        self.children_button.config(cursor='hand2')
        self.children_button.pack(side=ttk.TOP, fill=ttk.BOTH, expand=ttk.YES)

        self.adults_button = ttk.Button(self)
        self.adults_button.config(text='Adultos')
        self.adults_button.config(image=self.adults_img, compound=tk.TOP)
        self.adults_button.config(cursor='hand2')
        self.adults_button.pack(side=ttk.TOP, fill=ttk.BOTH, expand=ttk.YES)

        # noinspection PyArgumentList
        self.home_button.config(bootstyle=self.default_bootstyle)

        # noinspection PyArgumentList
        self.children_button.config(bootstyle=self.default_bootstyle)

        # noinspection PyArgumentList
        self.adults_button.config(bootstyle=self.default_bootstyle)

    def reset_bootstyle(self) -> None:
        """
        Reset the bootstyle for all navigation buttons to the default.

        This method sets the bootstyle of all navigation buttons to the default style.

        :return: None
        """
        for button in self.get_buttons():
            # noinspection PyArgumentList
            button.config(bootstyle=self.default_bootstyle)

    def focus_home_button(self) -> None:
        """
        Set the home button to the focused bootstyle.

        This method sets the home button's bootstyle to the focused style.

        :return: None
        """
        # noinspection PyArgumentList
        self.home_button.config(bootstyle=self.focus_bootstyle)

    def focus_children_button(self) -> None:
        """
        Set the children button to the focused bootstyle.

        This method sets the children button's bootstyle to the focused style.

        :return: None
        """
        # noinspection PyArgumentList
        self.children_button.config(bootstyle=self.focus_bootstyle)

    def focus_adults_button(self) -> None:
        """
        Set the adults button to the focused bootstyle.

        This method sets the adults button's bootstyle to the focused style.

        :return: None
        """
        # noinspection PyArgumentList
        self.adults_button.config(bootstyle=self.focus_bootstyle)

    def get_buttons(self) -> Tuple[ttk.Button, ...]:
        """
        Get a tuple of all navigation buttons.

        This method returns a tuple containing all the navigation buttons in the NavBar widget.

        :return: A tuple of navigation buttons.
        """
        return self.home_button, self.children_button, self.adults_button
