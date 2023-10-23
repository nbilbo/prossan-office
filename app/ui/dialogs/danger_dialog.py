import tkinter as tk

from app import constants
from app.ui.dialogs import InfoDialog
from app.utils.images import image_tk


class DangerDialog(InfoDialog):
    def __init__(self, master: tk.Misc, title: str, message: str) -> None:
        super().__init__(master, title, message)
        self.danger_img = image_tk(constants.ICONS_DIR / 'danger.png', (32, 32))
        self.label_message.config(image=self.danger_img)
