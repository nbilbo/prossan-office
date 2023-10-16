import tkinter as tk

import ttkbootstrap as ttk

from app import constants
from app.utils.images import image_tk


class Toolbar(ttk.Frame):
    """
    A custom widget for a toolbar with various actions.

    This widget provides a toolbar with buttons for actions such as zooming, changing themes, etc.
    """

    def __init__(self, master: tk.Misc) -> None:
        """
        Initialize the Toolbar widget.

        :param master: The parent widget to which this widget will be attached.
        """
        super().__init__(master)
        self.zoom_in_img = image_tk(constants.ICONS_DIR / 'zoom-in.png', (32, 32))
        self.zoom_out_img = image_tk(constants.ICONS_DIR / 'zoom-out.png', (32, 32))
        self.dark_mode_img = image_tk(constants.ICONS_DIR / 'dark-mode.png', (32, 32))
        self.light_mode_img = image_tk(constants.ICONS_DIR / 'light-mode.png', (32, 32))

        self.dark_theme_button = ttk.Button(self)
        self.dark_theme_button.config(image=self.dark_mode_img)
        self.dark_theme_button.config(cursor='hand2')
        self.dark_theme_button.pack(side=ttk.RIGHT)

        self.light_theme_button = ttk.Button(self)
        self.light_theme_button.config(image=self.light_mode_img)
        self.light_theme_button.config(cursor='hand2')
        self.light_theme_button.pack(side=ttk.RIGHT)
        self.light_theme_button.pack(side=ttk.RIGHT, padx=10)

        self.zoom_out_button = ttk.Button(self)
        self.zoom_out_button.config(image=self.zoom_out_img)
        self.zoom_out_button.config(cursor='hand2')
        self.zoom_out_button.pack(side=ttk.RIGHT)

        self.zoom_in_button = ttk.Button(self)
        self.zoom_in_button.config(image=self.zoom_in_img)
        self.zoom_in_button.config(cursor='hand2')
        self.zoom_in_button.pack(side=ttk.RIGHT, padx=10)

        # noinspection PyArgumentList
        self.dark_theme_button.config(bootstyle='default-link')

        # noinspection PyArgumentList
        self.light_theme_button.config(bootstyle='default-link')

        # noinspection PyArgumentList
        self.zoom_out_button.config(bootstyle='default-link')

        # noinspection PyArgumentList
        self.zoom_in_button.config(bootstyle='default-link')
