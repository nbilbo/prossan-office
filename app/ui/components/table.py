import tkinter as tk
from typing import List, Optional, Tuple, Union

import ttkbootstrap as ttk


class Table(ttk.Frame):
    """
    A custom widget for displaying tabular data.

    This widget provides a table view to display tabular data with rows and columns.
    """

    def __init__(self, master: tk.Misc) -> None:
        """
        Initialize the Table widget.

        :param master: The parent widget to which this widget will be attached.
        """
        super().__init__(master)
        self.pack_propagate(False)

        self.treeview = ttk.Treeview(self)
        self.treeview.pack(side=ttk.LEFT, fill=ttk.BOTH, expand=ttk.YES)

        self.vertical_scrollbar = ttk.Scrollbar(self, orient=ttk.VERTICAL)
        self.vertical_scrollbar.pack(side=ttk.RIGHT, fill=ttk.Y)

        self.treeview.config(yscrollcommand=self.vertical_scrollbar.set)
        self.vertical_scrollbar.config(command=self.treeview.yview)

    def clear_rows(self) -> None:
        """
        Clear all rows from the table.

        This method removes all rows (items) from the table.

        :return: None
        """
        self.treeview.delete(*self.treeview.get_children())

    def insert_row(self, row: Tuple[str, ...]) -> None:
        """
        Insert a row of data into the table.

        This method inserts a new row with the provided data into the table.

        :param row: The data to insert as a row.

        :return: None
        """
        self.treeview.insert('', tk.END, values=row)

    def get_selection(self) -> Optional[Tuple[str, ...]]:
        """
        Get the selected row from the table.

        This method retrieves the data from the selected row in the table.

        :return: The data from the selected row as a tuple, or None if no row is selected.
        """
        selections = self.treeview.selection()

        if selections:
            selection = selections[0]
            values = self.treeview.item(selection)['values']
            return tuple(str(value) for value in values)

        return None

    def set_columns(self, columns: Union[List[str], Tuple[str, ...]]) -> None:
        """
        Set the columns for the table.

        This method configures the columns and headings for the table view.

        :param columns: The column names to set.

        :return: None
        """
        self.treeview.config(columns=columns)
        self.treeview.config(show='headings')

        for column in columns:
            self.treeview.heading(column, text=column)
            self.treeview.column(column, width=50, minwidth=50, stretch=True, anchor=tk.CENTER)
