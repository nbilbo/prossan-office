import tkinter as tk

import ttkbootstrap as ttk

from app import constants
from app.utils import images


class Footer(ttk.Frame):
    """
    A custom widget for displaying footer information.

    This widget is typically placed at the bottom of an application window and can be used to display date and time
    information along with icons or other content.
    """

    def __init__(self, master: tk.Misc) -> None:
        """
        Initialize the Footer widget.

        :param master: The parent widget to which this widget will be attached.
        """
        super().__init__(master)
        self.calendar_img = images.image_tk(constants.ICONS_DIR / 'calendar.png', (32, 32))

        self.date_time_label = ttk.Label(self)
        self.date_time_label.config(text='date')
        self.date_time_label.config(image=self.calendar_img, compound=tk.LEFT)
        self.date_time_label.pack(side=ttk.RIGHT)
