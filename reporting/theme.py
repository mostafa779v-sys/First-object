"""
====================================================
BrainVisionAI
Professional Reporting Theme
v0.6
====================================================
"""

from PIL import ImageFont

# ==================================================
# Colors
# ==================================================

WHITE = (255, 255, 255)

BLACK = (25, 25, 25)

BACKGROUND = (246, 248, 252)

CARD = (255, 255, 255)

BORDER = (218, 222, 230)

LIGHT_GRAY = (150, 150, 150)

GRAY = (110, 110, 110)

PRIMARY = (25, 70, 135)

SECONDARY = (52, 152, 219)

SUCCESS = (39, 174, 96)

WARNING = (243, 156, 18)

DANGER = (220, 53, 69)

# ==================================================
# Report Resolution
# ==================================================

# High Resolution (Almost A4 @300 DPI)

PAGE_WIDTH = 3200

PAGE_HEIGHT = 2400

HEADER_HEIGHT = 180

FOOTER_HEIGHT = 100

MARGIN = 80

CARD_RADIUS = 35

CARD_BORDER = 3

# ==================================================
# Images
# ==================================================

IMAGE_WIDTH = 1100

IMAGE_HEIGHT = 1100

IMAGE_PADDING = 25

# ==================================================
# Font Loader
# ==================================================

def load_font(size, bold=False):

    if bold:

        candidates = [

            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",

            "arialbd.ttf",

            "/Library/Fonts/Arial Bold.ttf"

        ]

    else:

        candidates = [

            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",

            "arial.ttf",

            "/Library/Fonts/Arial.ttf"

        ]

    for path in candidates:

        try:

            return ImageFont.truetype(path, size)

        except:

            pass

    return ImageFont.load_default()

# ==================================================
# Fonts
# ==================================================

TITLE_FONT = load_font(82, True)

HEADER_FONT = load_font(54, True)

SECTION_FONT = load_font(42, True)

BIG_FONT = load_font(70, True)

TEXT_FONT = load_font(34)

SMALL_FONT = load_font(28)

PERCENT_FONT = load_font(52, True)

TINY_FONT = load_font(24)

# ==================================================
# Layout
# ==================================================

SHADOW_OFFSET = 8

CARD_PADDING = 35

LINE_SPACING = 12

SECTION_SPACING = 45

IMAGE_CORNER_RADIUS = 18

BAR_HEIGHT = 34

BAR_RADIUS = 17
