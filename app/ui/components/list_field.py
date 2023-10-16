import tkinter as tk
from functools import partial
from typing import List, Tuple, Union

import ttkbootstrap as ttk

from app import constants
from app.utils.images import image_tk


class ListItem(ttk.Frame):
    """
    A custom widget representing an item in a list.

    This widget displays an item in a list with a label and a remove button.
    """

    def __init__(self, master: tk.Misc) -> None:
        """
        Initialize the ListItem widget.

        :param master: The parent widget to which this widget will be attached.
        """
        super().__init__(master)
        self.minus_img = image_tk(constants.ICONS_DIR / 'minus.png', (16, 16))

        index_label = ttk.Label(self)
        index_label.config(text='•')
        index_label.pack(side=tk.LEFT)

        self.label = ttk.Label(self)
        self.label.config(width=1)
        self.label.pack(side=tk.LEFT, fill=tk.X, expand=tk.YES)

        self.remove_button = ttk.Button(self)
        self.remove_button.config(cursor='hand2')
        self.remove_button.config(image=self.minus_img)
        self.remove_button.pack(side=tk.LEFT)

        # noinspection PyArgumentList
        self.remove_button.config(bootstyle='default-link')


class ListField(ttk.Labelframe):
    """
    A custom widget for managing a list of items.

    This widget allows users to add and remove items from a list.
    """

    def __init__(self, master: tk.Misc) -> None:
        """
        Initialize the ListField widget.

        :param master: The parent widget to which this widget will be attached.
        """
        super().__init__(master)
        self.plus_img = image_tk(constants.ICONS_DIR / 'plus.png', (16, 16))
        self.items: List[ListItem] = []

        container = ttk.Frame(self)
        container.config(padding=10)
        container.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES)

        self.actions_container = ttk.Frame(container)
        self.actions_container.config(width=1)
        self.actions_container.pack(side=tk.TOP, fill=tk.X)

        self.entry = ttk.Entry(self.actions_container)
        self.entry.config(width=1)
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=tk.YES)
        self.entry.bind('<Return>', lambda event: self.handle_add_item())

        self.add_button = ttk.Button(self.actions_container)
        self.add_button.config(cursor='hand2')
        self.add_button.config(image=self.plus_img)
        self.add_button.config(command=self.handle_add_item)
        self.add_button.pack(side=tk.LEFT, fill=tk.BOTH)

        self.items_container = ttk.Frame(container)
        self.items_container.config(width=1)
        self.items_container.pack(side=tk.TOP, fill=tk.X)

        # noinspection PyArgumentList
        # self.config(bootstyle='info')
        self.add_button.config(bootstyle='default-link')

    def clear_items_container(self) -> None:
        """
        Clear the items container by destroying all child widgets.

        This method removes all child widgets within the items container, effectively clearing the list of items
        displayed in the widget.

        :return: None
        """
        for children in self.items_container.winfo_children():
            children.destroy()

    def add_list_item(self, item: str) -> None:
        """
        Add a new item to the list.

        This method creates a new ListItem widget to represent the provided item, sets its label text, adds it
        to the list of items, and binds the removal action to it.

        :param item: The item to add to the list.

        :return: None
        """
        list_item = ListItem(self.items_container)
        list_item.label.config(text=item)
        list_item.pack(side=tk.TOP, fill=tk.X, pady=10)
        self.items.append(list_item)
        self.bind_list_item(list_item)

    def bind_list_item(self, list_item: ListItem) -> None:
        """
        Bind a removal action to a list item.

        This method associates a removal action with the specified list item's remove button. When the remove button
        is clicked, it triggers the removal action.

        :param list_item: The ListItem widget to which the removal action will be bound.

        :return: None
        """
        command = partial(self.handle_remove_item, list_item)
        list_item.remove_button.config(command=command)

    def handle_add_item(self) -> None:
        """
        Handle the addition of a new item to the list.

        This method retrieves the item from the entry field, adds it to the list, clears the entry field,
        and refocuses on it.

        :return: None
        """
        item = self.entry.get().strip()

        if len(item):
            self.add_list_item(item)
            self.entry.delete(0, tk.END)

        self.entry.focus()

    def handle_remove_item(self, item: ListItem) -> None:
        """
        Handle the removal of a list item.

        This method removes the specified list item from the list and destroys it. It also refocuses on the entry
        field for adding new items.

        :param item: The ListItem widget to be removed.

        :return: None
        """
        item.destroy()
        self.items.remove(item)
        self.entry.focus()

    def get_value(self) -> List[str]:
        """
        Get the list of values currently displayed in the ListField.

        This method retrieves the text values from the labels of all items in the list and returns them as a list.

        :return: A list of text values from the list items.
        """
        return [item.label.cget('text') for item in self.items]

    def set_value(self, value: Union[List[str], Tuple[str, ...]]) -> None:
        """
        Set the list of values to be displayed in the ListField.

        This method clears the existing list of items, then adds new list items to represent the provided values.

        :param value: The list of values to be displayed in the ListField.
        """
        self.clear_items_container()
        self.items.clear()

        for item in value:
            self.add_list_item(item)
