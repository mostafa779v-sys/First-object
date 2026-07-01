"""
====================================================
BrainVisionAI
Reporting Helpers
====================================================
"""

import os

from PIL import Image

# ====================================================
# Image Loader
# ====================================================

def load_image(image):

    """
    Accepts:

    - Image path

    - PIL Image

    Returns PIL.Image
    """

    if isinstance(image, Image.Image):

        return image.copy()

    if isinstance(image, str):

        if not os.path.exists(image):

            raise FileNotFoundError(image)

        return Image.open(image).convert("RGB")

    raise TypeError(

        "Unsupported image type."

    )


# ====================================================
# Resize While Keeping Aspect Ratio
# ====================================================

def fit_image(

    image,

    max_width,

    max_height

):

    image = image.copy()

    image.thumbnail(

        (

            max_width,

            max_height

        )

    )

    return image


# ====================================================
# Center Position
# ====================================================

def center_position(

    outer_width,

    outer_height,

    inner_width,

    inner_height

):

    x = (

        outer_width -

        inner_width

    ) // 2

    y = (

        outer_height -

        inner_height

    ) // 2

    return x, y


# ====================================================
# Percentage Clamp
# ====================================================

def clamp_percentage(value):

    value = float(value)

    if value < 0:

        return 0.0

    if value > 100:

        return 100.0

    return value


# ====================================================
# Format Percentage
# ====================================================

def format_percentage(value):

    return f"{clamp_percentage(value):.2f}%"


# ====================================================
# Safe Text
# ====================================================

def safe_text(value):

    if value is None:

        return ""

    return str(value)
