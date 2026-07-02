"""
====================================================
BrainVisionAI
Professional Image Components
====================================================
"""

from PIL import (
    Image,
    ImageOps
)

from . import theme


# =====================================================
# Image Panel
# =====================================================

class ImagePanel:

    def __init__(

        self,

        canvas,

        image,

        title,

        x,

        y,

        width=theme.IMAGE_WIDTH,

        height=theme.IMAGE_HEIGHT

    ):

        self.canvas = canvas

        self.image = image

        self.title = title

        self.x = x

        self.y = y

        self.width = width

        self.height = height

    # =================================================

    def _prepare_image(self):

        if isinstance(self.image, str):

            img = Image.open(

                self.image

            ).convert(

                "RGB"

            )

        else:

            img = self.image.copy()

        img.thumbnail(

            (

                self.width - 80,

                self.height - 130

            ),

            Image.Resampling.LANCZOS

        )

        return img

    # =================================================

    def draw(self):

        # ---------------------------------------------
        # Shadow
        # ---------------------------------------------

        self.canvas.shadow_box(

            self.x,

            self.y,

            self.width,

            self.height

        )

        # ---------------------------------------------
        # Card
        # ---------------------------------------------

        self.canvas.rounded_box(

            self.x,

            self.y,

            self.width,

            self.height

        )

        # ---------------------------------------------
        # Card Title
        # ---------------------------------------------

        self.canvas.text(

            self.x + 35,

            self.y + 25,

            self.title,

            theme.SECTION_FONT,

            theme.PRIMARY

        )

        # ---------------------------------------------
        # Divider
        # ---------------------------------------------

        self.canvas.line(

            self.x + 30,

            self.y + 85,

            self.x + self.width - 30,

            self.y + 85,

            theme.BORDER,

            2

        )

        # ---------------------------------------------
        # Image
        # ---------------------------------------------

        img = self._prepare_image()

        frame = ImageOps.expand(

            img,

            border=4,

            fill=theme.BORDER

        )

        offset_x = (

            self.width -

            frame.width

        ) // 2

        offset_y = (

            self.height -

            frame.height

        ) // 2 + 35

        self.canvas.image.paste(

            frame,

            (

                self.x + offset_x,

                self.y + offset_y

            )

        )

        # ---------------------------------------------
        # Bottom Information
        # ---------------------------------------------

        info_y = self.y + self.height - 55

        self.canvas.line(

            self.x + 30,

            info_y - 18,

            self.x + self.width - 30,

            info_y - 18,

            theme.BORDER,

            2

        )

        self.canvas.text(

            self.x + 35,

            info_y,

            f"Resolution : {img.width} × {img.height}",

            theme.SMALL_FONT,

            theme.GRAY

        )

        self.canvas.text(

            self.x + self.width - 280,

            info_y,

            "BrainVisionAI",

            theme.SMALL_FONT,

            theme.SECONDARY

        )
        # =====================================================
# MRI Section
# =====================================================

class MRISection:

    """
    Draw Original MRI
    +
    Grad-CAM
    """

    def __init__(

        self,

        canvas,

        original_image,

        gradcam_image

    ):

        self.canvas = canvas

        self.original = original_image

        self.gradcam = gradcam_image

    # =================================================

    def draw(self):

        top = theme.HEADER_HEIGHT + 70

        left_margin = 80

        gap = 80

        panel_width = theme.IMAGE_WIDTH

        panel_height = theme.IMAGE_HEIGHT

        original_panel = ImagePanel(

            self.canvas,

            self.original,

            "Original MRI Scan",

            left_margin,

            top,

            panel_width,

            panel_height

        )

        gradcam_panel = ImagePanel(

            self.canvas,

            self.gradcam,

            "Grad-CAM Visualization",

            left_margin + panel_width + gap,

            top,

            panel_width,

            panel_height

        )

        original_panel.draw()

        gradcam_panel.draw()
        # =====================================================
# Future Extension
# =====================================================

class ComparisonSection:

    """
    Reserved for future versions.

    v0.7:
        Before / After MRI

    v0.8:
        Multiple MRI slices

    v1.0:
        Automatic lesion comparison
    """

    pass
