import tkinter as tk
from typing import Tuple

import ttkbootstrap as ttk

from app import constants
from app.ui.components import DropdownField, SpinField


class HousingField(ttk.Labelframe):
    """
    A custom widget for entering and displaying housing information.

    This widget includes fields for the type housing, paid monthly.
    """

    def __init__(self, master: tk.Misc) -> None:
        """
        Initialize the HousingField widget.

        :param master: The parent widget to which this widget will be attached.
        """
        super().__init__(master)
        self.config(text='Moradia')

        container = ttk.Frame(self)
        container.config(padding=10)
        container.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.type_housing_field = DropdownField(container)
        self.type_housing_field.label.config(text='Tipo')
        self.type_housing_field.set_options(constants.TYPE_HOUSING)
        self.type_housing_field.pack(side=tk.TOP, fill=tk.X)
        ttk.Frame(container).pack(side=tk.TOP, fill=tk.X, pady=10)

        self.paid_monthly_field = SpinField(container)
        self.paid_monthly_field.label.config(text='Valor mensal')
        self.paid_monthly_field.spinbox.config(from_=0, to=9999, format='%.2f')
        self.paid_monthly_field.set_value('0000,00')
        self.paid_monthly_field.pack(side=tk.TOP, fill=tk.X)
        ttk.Frame(container).pack(side=tk.TOP, fill=tk.X, pady=10)

    def get_value(self) -> Tuple[str, str]:
        """
        Get the values of the housing fields.

        :return: A tuple containing the values of the type housing and paid monthly fields.
        """
        return self.type_housing_field.get_value(), self.paid_monthly_field.get_value()

    def set_value(self, value: Tuple[str, str]) -> None:
        """
        Set the values of the housing fields.

        :param value: A tuple containing the values for the type housing and paid monthly fields.
        """
        self.type_housing_field.set_value(value[0])
        self.paid_monthly_field.set_value(value[1])
