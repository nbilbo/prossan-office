import tkinter as tk

import ttkbootstrap as ttk

from app import constants
from app.utils.images import image_tk


class InfoDialog(ttk.Toplevel):
    def __init__(self, master: tk.Misc, title: str, message: str) -> None:
        super().__init__(master=master)
        self.title(title)
        self.attributes('-topmost', 'true')

        self.confirm_img = image_tk(constants.ICONS_DIR / 'confirm.png', (32, 32))
        self.info_img = image_tk(constants.ICONS_DIR / 'info.png', (32, 32))

        self.container = ttk.Frame(self)
        self.container.config(padding=10)
        self.container.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES)

        self.container.grid_columnconfigure(0, weight=1)
        self.container.grid_rowconfigure(1, weight=1)

        self.label_message = ttk.Label(self.container)
        self.label_message.config(text=message)
        self.label_message.config(image=self.info_img, compound=tk.LEFT)
        self.label_message.grid(row=0, column=0, columnspan=2)

        self.confirm_button = ttk.Button(self.container)
        self.confirm_button.config(text='Confirmar')
        self.confirm_button.config(cursor='hand2')
        self.confirm_button.config(image=self.confirm_img, compound=tk.RIGHT)
        self.confirm_button.config(command=self.destroy)
        self.confirm_button.grid(row=1, column=1, sticky=tk.SE, pady=10)
        self.confirm_button.focus()

        # noinspection PyArgumentList
        self.confirm_button.config(bootstyle='default-link')
