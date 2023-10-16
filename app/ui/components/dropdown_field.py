import tkinter as tk
from typing import List, Tuple, Union

import ttkbootstrap as ttk


class DropdownField(ttk.Frame):
    """
    A custom widget for selecting options from a dropdown.

    This widget combines a label and a combobox for selecting options. It can be used to represent
    a dropdown field in a user interface.

    :param master: The parent widget to which this widget will be attached.
    """

    def __init__(self, master: tk.Misc) -> None:
        """
        Initialize the DropdownField widget.

        :param master: The parent widget to which this widget will be attached.
        """
        super().__init__(master)
        self.label = ttk.Label(self)
        self.label.config(width=1)
        self.label.config(cursor='hand2')
        self.label.pack(side=tk.LEFT, fill=tk.X, expand=True)

        self.combobox_var = tk.StringVar()
        self.combobox = ttk.Combobox(self)
        self.combobox.config(textvariable=self.combobox_var)
        self.combobox.config(width=1)
        self.combobox.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.label.bind('<ButtonRelease-1>', lambda event: self.combobox.focus())

    def set_options(self, options: Union[List[str], Tuple[str, ...]]) -> None:
        """
        Set the available options in the dropdown.

        :param options: A list or tuple of strings representing the available options.

        :return: None
        """
        self.combobox_var.set(options[0])
        self.combobox.config(values=options)

    def set_value(self, value: str) -> None:
        """
        Set the selected value in the dropdown.

        :param value: The value to set as the selected option in the dropdown.

        :return: None
        """
        self.combobox_var.set(value)

    def get_value(self) -> str:
        """
        Get the currently selected value from the dropdown.

        :return: The currently selected value from the dropdown.
        """
        return self.combobox_var.get()
