import tkinter as tk

import ttkbootstrap as ttk


class RadioField(ttk.LabelFrame):
    """
    A custom widget for select a single option.
    """

    def __init__(self, master: tk.Misc) -> None:
        """
        Initialize the RadioField widget.

        :param master: The parent widget to which this widget will be attached.
        """
        super().__init__(master)
        self.radio_var = tk.StringVar()
        self.config(padding=10)

        self.label = ttk.Label(self)
        self.label.config(width=1)
        self.label.config(cursor='hand2')
        self.label.pack(side=tk.LEFT, fill=tk.X, expand=tk.YES, anchor=tk.N)

        self.radios_container = ttk.Frame(self)
        self.radios_container.config(width=1)
        self.radios_container.pack(side=tk.LEFT, fill=tk.X, expand=tk.YES)

    def add_option(self, text: str, value: str) -> None:
        """
        Add a radio button option to the RadioField.

        :param text: The text label for the radio button.
        :param value: The value associated with the radio button.
        """
        radio = ttk.Radiobutton(self.radios_container)
        radio.config(text=text, value=value, variable=self.radio_var)
        radio.config(cursor='hand2')
        radio.pack(side=tk.TOP, fill=tk.X, anchor=tk.CENTER)
        ttk.Frame(self.radios_container).pack(side=tk.TOP, pady=10)

    def set_value(self, value: str) -> None:
        """
        Set the value of the selected radio button.

        :param value: The value to set for the selected radio button.
        """
        self.radio_var.set(value)

    def get_value(self) -> str:
        """
        Get the value of the selected radio button.

        :return: The value of the selected radio button as a string.
        """
        return self.radio_var.get()
