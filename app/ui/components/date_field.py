import tkinter as tk

import ttkbootstrap as ttk


class DateField(ttk.Frame):
    def __init__(self, master: tk.Misc) -> None:
        super().__init__(master)
        self.label = ttk.Label(self)
        self.label.config(width=1)
        self.label.pack(side=tk.LEFT, fill=tk.X, expand=tk.YES)

        self.entry = ttk.Entry(self)
        self.entry.config(width=1)
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=tk.YES)
