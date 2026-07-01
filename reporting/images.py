"""
====================================================
BrainVisionAI
Image Components
====================================================
"""

from PIL import Image

from . import theme


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

    # =========================================

    def _prepare_image(self):

        if isinstance(self.image, str):

            img = Image.open(self.image).convert("RGB")

        else:

            img = self.image.copy()

        img.thumbnail(

            (

                self.width -

                theme.IMAGE_PADDING * 2,

                self.height -

                theme.IMAGE_PADDING * 2

            )

        )

        return img

    # =========================================

    def draw(self):

        self.canvas.shadow_box(

            self.x,

            self.y,

            self.width,

            self.height

        )

        img = self._prepare_image()

        offset_x = (

            self.width -

            img.width

        ) // 2

        offset_y = (

            self.height -

            img.height

        ) // 2

        self.canvas.image.paste(

            img,

            (

                self.x +

                offset_x,

                self.y +

                offset_y

            )

        )

        self.canvas.text(

            self.x,

            self.y - 40,

            self.title,

            theme.HEADER_FONT,

            theme.PRIMARY

        )


# =====================================================

class MRISection:

    """
    Draw Original MRI
    +
    GradCAM
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

    # =========================================

    def draw(self):

        left = ImagePanel(

            self.canvas,

            self.original,

            "Original MRI",

            70,

            170

        )

        right = ImagePanel(

            self.canvas,

            self.gradcam,

            "Grad-CAM",

            880,

            170

        )

        left.draw()

        right.draw()
