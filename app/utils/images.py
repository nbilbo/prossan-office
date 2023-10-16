from pathlib import Path
from typing import Tuple

from PIL import Image, ImageTk


def image_tk(path: Path, size: Tuple[int, int] = None):
    """
    Load an image from the given file path and convert it to a PhotoImage object.

    :param path: The file path to the image.
    :param size: Optional. The size (width, height) to resize the image to.

    :return: A PhotoImage object representing the loaded image (optionally resized).
    """
    image = Image.open(path)
    if size is not None:
        image = image.resize(size)
    photo_image = ImageTk.PhotoImage(image)
    return photo_image
