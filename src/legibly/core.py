"""Core functions of legibly. (examples for documentation)"""


def resize(path, width):
    """Resize an image to the given width, keeping its aspect ratio.

    Args:
        path (str): Path to the input image file.
        width (int): Target width in pixels. Must be positive.

    Returns:
        PIL.Image.Image: The resized image. The height is computed
        from the original aspect ratio.

    Raises:
        ValueError: If ``width`` is not a positive integer.

    Examples:
        >>> resize("examples/clock.png", 200).size
        (200, 100)
    """
    raise NotImplementedError


def crop(path, box):
    """Crop an image to a rectangle.

    Args:
        path (str): Path to the input image file.
        box (tuple[int, int, int, int]): (left, top, right, bottom) in pixels.

    Returns:
        PIL.Image.Image: The cropped image.

    Examples:
        >>> crop("examples/clock.png", (0, 0, 100, 100)).size
        (100, 100)
    """
    raise NotImplementedError


def grayscale(path, out):
    """Save a grayscale copy of an image. The original file is not changed.

    Args:
        path (str): Path to the input image file.
        out (str): Path of the new grayscale file. Must differ from ``path``.

    Returns:
        str: The path of the file that was written.

    Examples:
        >>> grayscale("examples/clock.png", "clock_gray.png")
        'clock_gray.png'
    """
    raise NotImplementedError
