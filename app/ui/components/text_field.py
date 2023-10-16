import tkinter as tk

import ttkbootstrap as ttk


class TextField(ttk.Frame):
    """
    A custom widget for text input with a label.

    This widget provides a label and an entry field for text input.
    """

    def __init__(self, master: tk.Misc) -> None:
        """
        Initialize the TextField widget.

        :param master: The parent widget to which this widget will be attached.
        """
        super().__init__(master)
        self.label = ttk.Label(self)
        self.label.config(width=1)
        self.label.config(cursor='hand2')
        self.label.pack(side=tk.LEFT, fill=tk.X, expand=tk.YES)

        self.entry = ttk.Entry(self)
        self.entry.config(width=1)
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=tk.YES)
        self.label.bind('<ButtonRelease-1>', lambda event: self.entry.focus())

    def get_value(self) -> str:
        """
        Get the text value from the input field.

        This method retrieves the text value entered into the input field.

        :return: The text value from the input field.
        """
        value = self.entry.get()
        return value.strip() if value is not None else ''

    def set_value(self, value: str) -> None:
        """
        Set the text value in the input field.

        This method sets the text value in the input field.

        :param value: The text value to set in the input field.

        :return: None
        """
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, value)
