from PIL import Image
import numpy as np


def load_maze(image_path, threshold=128):
    """Load a maze image and return a binary 2D numpy array and the PIL image.

    Pixels darker than `threshold` become walls (0), lighter ones become paths (1).
    """
    image = Image.open(image_path).convert("L")
    binary = image.point(lambda p: 1 if p > threshold else 0)
    grid = np.array(binary)
    return grid, image


def draw_path(image, path, color=150):
    """Draw the solved path onto the image in-place."""
    pixels = image.load()
    for node in path:
        pixels[node.y, node.x] = color
    return image
