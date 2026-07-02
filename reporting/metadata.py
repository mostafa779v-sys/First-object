"""
====================================================
BrainVisionAI
Professional Metadata Section
====================================================
"""

from datetime import datetime

from . import theme


class MetadataSection:

    def __init__(

        self,

        canvas,

        model_name,

        version,

        device,

        image_size

    ):

        self.canvas = canvas

        self.model_name = model_name

        self.version = version

        self.device = device

        self.image_size = image_size

    # =================================================

    def draw_item(

        self,

        x,

        y,

        title,

        value

    ):

        self.canvas.text(

            x,

            y,

            title,

            theme.SMALL_FONT,

            theme.GRAY

        )

        self.canvas.text(

            x,

            y + 42,

            str(value),

            theme.TEXT_FONT,

            theme.BLACK

        )

    # =================================================

    def draw(self):

        x = 80

        y = 2120

        width = theme.PAGE_WIDTH - 160

        height = 180

        # ------------------------------------------
        # Card
        # ------------------------------------------

        self.canvas.shadow_box(

            x,

            y,

            width,

            height

        )

        self.canvas.rounded_box(

            x,

            y,

            width,

            height

        )

        self.canvas.text(

            x + 35,

            y + 22,

            "Model Information",

            theme.HEADER_FONT,

            theme.PRIMARY

        )

        self.canvas.line(

            x + 30,

            y + 75,

            x + width - 30,

            y + 75,

            theme.BORDER,

            2

        )

        info_y = y + 95

        self.draw_item(

            x + 40,

            info_y,

            "Model",

            self.model_name

        )

        self.draw_item(

            x + 500,

            info_y,

            "Version",

            self.version

        )

        self.draw_item(

            x + 900,

            info_y,

            "Device",

            self.device.upper()

        )

        self.draw_item(

            x + 1300,

            info_y,

            "Input Size",

            f"{self.image_size} × {self.image_size}"

        )

        self.draw_item(

            x + 1850,

            info_y,

            "Generated",

            datetime.now().strftime(

                "%Y-%m-%d %H:%M"

            )

        )
