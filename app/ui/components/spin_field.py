import tkinter as tk

import ttkbootstrap as ttk


class SpinField(ttk.Frame):
    """A custom spin field widget."""

    def __init__(self, master: tk.Misc) -> None:
        """
        Initialize the SpinField widget.

        :param master: The parent widget to which this widget will be attached.
        """
        super().__init__(master)
        self.label = ttk.Label(self)
        self.label.config(width=1)
        self.label.config(cursor='hand2')
        self.label.pack(side=tk.LEFT, fill=tk.X, expand=tk.YES)

        self.spin_var = tk.StringVar()
        self.spinbox = ttk.Spinbox(self)
        self.spinbox.config(textvariable=self.spin_var)
        self.spinbox.config(width=1)
        self.spinbox.pack(side=tk.LEFT, fill=tk.X, expand=tk.YES)
        self.label.bind('<ButtonRelease-1>', lambda event: self.spinbox.focus())

    def set_value(self, value: str) -> None:
        """
        Set the value displayed in the SpinField.

        :param value: The value to set in the SpinField.
        """
        self.spinbox.set(value)

    def get_value(self) -> str:
        """
        Retrieve the current value from the SpinField.

        :return: The current value in the SpinField as a string.
        """
        return self.spin_var.get().strip()
