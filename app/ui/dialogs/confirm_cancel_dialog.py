import tkinter as tk
from typing import Callable

import ttkbootstrap as ttk

from app import constants
from app.utils.images import image_tk


class ConfirmCancelDialog(ttk.Toplevel):
    """
    A custom widget for a confirmation dialog with confirm and cancel buttons.

    This widget provides a modal dialog with a message and options to confirm or cancel an action.
    """

    def __init__(self, master: tk.Misc, title: str, message: str, command: Callable) -> None:
        """
        Initialize the ConfirmCancelDialog widget.

        :param master: The parent widget.
        :param title: The title of the dialog window.
        :param message: The message displayed in the dialog.
        :param command: The function to be executed when the confirm button is clicked.
        """
        super().__init__(master=master)
        self.command = command
        self.confirm_img = image_tk(constants.ICONS_DIR / 'confirm.png', (32, 32))
        self.cancel_img = image_tk(constants.ICONS_DIR / 'cancel.png', (32, 32))
        self.title(title)

        container = ttk.Frame(self)
        container.config(padding=10)
        container.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES)

        self.label_message = ttk.Label(container)
        self.label_message.config(text=message)
        self.label_message.config(anchor=tk.CENTER)
        self.label_message.pack(side=tk.TOP, fill=tk.X, pady=10)

        actions_container = ttk.Frame(container)
        actions_container.pack(side=tk.BOTTOM, anchor=tk.E)

        self.confirm_button = ttk.Button(actions_container)
        self.confirm_button.config(text='Confirmar')
        self.confirm_button.config(image=self.confirm_img, compound=tk.RIGHT)
        self.confirm_button.config(cursor='hand2')
        self.confirm_button.config(command=self.handle_confirm)
        self.confirm_button.pack(side=tk.LEFT, padx=10)

        self.cancel_button = ttk.Button(actions_container)
        self.cancel_button.config(text='Cancelar')
        self.cancel_button.config(image=self.cancel_img, compound=tk.RIGHT)
        self.cancel_button.config(cursor='hand2')
        self.cancel_button.config(command=self.handle_cancel)
        self.cancel_button.pack(side=tk.LEFT)

        # noinspection PyArgumentList
        self.confirm_button.config(bootstyle='success-link')

        # noinspection PyArgumentList
        self.cancel_button.config(bootstyle='danger-link')

    def handle_confirm(self) -> None:
        """
        Execute the confirmation action and close the dialog.

        This method executes the confirmation action (specified during widget creation) and closes the dialog window.

        :return: None
        """
        self.command()
        self.destroy()

    def handle_cancel(self) -> None:
        """
        Close the dialog without taking any action.

        This method simply closes the dialog without performing any action.

        :return: None
        """
        self.destroy()
