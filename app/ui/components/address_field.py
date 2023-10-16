import tkinter as tk
from typing import Tuple

import ttkbootstrap as ttk

from app.ui.components import TextField


class AddressField(ttk.Labelframe):
    """
    A custom widget for entering and displaying address information.

    This widget includes fields for the street, district, city, and state of an address.
    """

    def __init__(self, master: tk.Misc) -> None:
        """
        Initialize the AddressField widget.

        :param master: The parent widget to which this widget will be attached.
        """
        super().__init__(master)
        self.config(text='Endereço')

        container = ttk.Frame(self)
        container.config(padding=10)
        container.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.street_field = TextField(container)
        self.street_field.label.config(text='Rua')
        self.street_field.pack(side=tk.TOP, fill=tk.X)
        ttk.Frame(container).pack(side=tk.TOP, fill=tk.X, pady=10)

        self.district_field = TextField(container)
        self.district_field.label.config(text='Bairro')
        self.district_field.pack(side=tk.TOP, fill=tk.X)
        ttk.Frame(container).pack(side=tk.TOP, fill=tk.X, pady=10)

        self.city_field = TextField(container)
        self.city_field.label.config(text='Cidade')
        self.city_field.pack(side=tk.TOP, fill=tk.X)
        ttk.Frame(container).pack(side=tk.TOP, fill=tk.X, pady=10)

        self.state_field = TextField(container)
        self.state_field.label.config(text='Estado')
        self.state_field.pack(side=tk.TOP, fill=tk.X)
        ttk.Frame(container).pack(side=tk.TOP, fill=tk.X, pady=10)

    def get_value(self) -> Tuple[str, str, str, str]:
        """
        Get the values of the address fields.

        :return: A tuple containing the values of the street, district, city, and state fields.
        """
        street = self.street_field.get_value()
        district = self.district_field.get_value()
        city = self.city_field.get_value()
        state = self.state_field.get_value()
        return street, district, city, state

    def set_value(self, value: Tuple[str, str, str, str]) -> None:
        """
        Set the values of the address fields.

        :param value: A tuple containing the values for the street, district, city, and state fields.
        """
        self.street_field.set_value(value[0])
        self.district_field.set_value(value[1])
        self.city_field.set_value(value[2])
        self.state_field.set_value(value[3])
