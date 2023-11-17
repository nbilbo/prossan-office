import tkinter as tk
from pathlib import Path
from tkinter import filedialog
from typing import Optional, Tuple

import ttkbootstrap as ttk

from app import constants
from app.ui.forms import BaseForm
from app.utils.images import image_tk


class DocumentForm(BaseForm):
    """
    A form for generating a document with a user-specified name and location.
    """

    def __init__(
        self,
        master: tk.Misc,
        initialfile: Optional[str] = None,
        initialdir: Optional[str] = None,
        filetypes: Optional[Tuple[Tuple[str, str], ...]] = None,
    ) -> None:
        """
        Initialize a new DocumentForm.

        :param master: The parent widget.
        :param initialfile: The initial filename to display in the form.
        :param initialdir: The initial directory to display in the form.
        :param filetypes: The filetypes.

        :return: None
        """

        super().__init__(master=master)
        self.title('Escritório do Prossan - Gerar documento')
        self.geometry('700x300')

        self.initialfile = initialfile
        self.initialdir = initialdir
        self.filetypes = filetypes

        self.start_img = image_tk(constants.ICONS_DIR / 'start.png', (32, 32))
        self.folder_img = image_tk(constants.ICONS_DIR / 'folder.png', (32, 32))

        self.inner_container = ttk.Frame(self.container)
        self.inner_container.grid_columnconfigure(1, weight=1)
        self.inner_container.pack(side=tk.TOP, fill=tk.BOTH)

        self.label = ttk.Label(self.inner_container)
        self.label.config(text='Nome do arquivo')
        self.label.grid(row=0, column=0, padx=5)

        self.entry = ttk.Entry(self.inner_container)
        self.entry.config(width=1)
        self.entry.grid(row=0, column=1, stick=tk.EW)

        self.dialog_button = ttk.Button(self.inner_container)
        self.dialog_button.config(cursor='hand2')
        self.dialog_button.config(image=self.folder_img, compound=tk.CENTER)
        self.dialog_button.config(command=self.handle_dialog)
        self.dialog_button.grid(row=0, column=2, padx=5)

        self.confirm_button = ttk.Button(self.inner_container)
        self.confirm_button.config(text='Gerar documento')
        self.confirm_button.config(cursor='hand2')
        self.confirm_button.config(image=self.start_img, compound=tk.RIGHT)
        self.confirm_button.grid(row=1, column=0, columnspan=3, stick=tk.EW, pady=10)

        # noinspection PyArgumentList
        self.dialog_button.config(bootstyle='primary-link')

        # noinspection PyArgumentList
        self.confirm_button.config(bootstyle='success-link')

        if self.initialdir is not None and self.initialfile is not None:
            self.set_value(Path.joinpath(self.initialdir, self.initialfile))

    def handle_dialog(self) -> None:
        """
        Open a file dialog to choose a file location.

        This method allows the user to select the directory and filename for the document.

        :return: None
        """
        initialfile, initialdir = self.initialfile, self.initialdir
        filetypes = self.filetypes if self.filetypes is not None else (('Todos arquivos', '.'),)

        self.attributes('-topmost', 'false')
        value = filedialog.asksaveasfilename(initialfile=initialfile, initialdir=initialdir, filetypes=filetypes)
        self.attributes('-topmost', 'true')

        if value is not None and len(value):
            self.set_value(value)

    def get_value(self) -> str:
        """
        Get the user-specified file location.

        :return: The selected file location.
        """
        return self.entry.get()

    def set_value(self, value: str) -> None:
        """
        Set the value of the file location in the form.

        :param value: The file location to set in the form.

        :return: None
        """
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, value)
