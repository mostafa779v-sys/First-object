"""
====================================================
BrainVisionAI
Professional Canvas Engine
====================================================
"""

import os

from PIL import (
    Image,
    ImageDraw
)

from . import theme


class ReportCanvas:

    def __init__(self):

        self.image = Image.new(

            "RGB",

            (

                theme.PAGE_WIDTH,

                theme.PAGE_HEIGHT

            ),

            theme.BACKGROUND

        )

        self.draw = ImageDraw.Draw(

            self.image

        )

    # =================================================

    def save(self, path):

        folder = os.path.dirname(path)

        if folder:

            os.makedirs(

                folder,

                exist_ok=True

            )

        self.image.save(path)

    # =================================================

    def rectangle(

        self,

        x,

        y,

        width,

        height,

        color

    ):

        self.draw.rectangle(

            (

                x,

                y,

                x + width,

                y + height

            ),

            fill=color

        )

    # =================================================

    def rounded_box(

        self,

        x,

        y,

        width,

        height,

        fill=theme.CARD,

        outline=theme.BORDER,

        radius=None,

        border_width=2

    ):

        if radius is None:

            radius = theme.CARD_RADIUS

        self.draw.rounded_rectangle(

            (

                x,

                y,

                x + width,

                y + height

            ),

            radius=radius,

            fill=fill,

            outline=outline,

            width=border_width

        )

    # =================================================

    def shadow_box(

        self,

        x,

        y,

        width,

        height,

        shadow=5

    ):

        self.draw.rounded_rectangle(

            (

                x + shadow,

                y + shadow,

                x + width + shadow,

                y + height + shadow

            ),

            radius=theme.CARD_RADIUS,

            fill=(210,210,210)

        )

        self.rounded_box(

            x,

            y,

            width,

            height

        )

    # =================================================

    def line(

        self,

        x1,

        y1,

        x2,

        y2,

        color=theme.BORDER,

        width=2

    ):

        self.draw.line(

            (

                x1,

                y1,

                x2,

                y2

            ),

            fill=color,

            width=width

        )

    # =================================================

    def circle(

        self,

        x,

        y,

        radius,

        fill,

        outline=None

    ):

        self.draw.ellipse(

            (

                x,

                y,

                x + radius * 2,

                y + radius * 2

            ),

            fill=fill,

            outline=outline

        )

    # =================================================

    def text(

        self,

        x,

        y,

        value,

        font,

        color=theme.BLACK,

        anchor=None

    ):

        self.draw.text(

            (

                x,

                y

            ),

            str(value),

            fill=color,

            font=font,

            anchor=anchor

        )

    # =================================================

    def centered_text(

        self,

        x,

        y,

        width,

        value,

        font,

        color=theme.BLACK

    ):

        bbox = self.draw.textbbox(

            (

                0,

                0

            ),

            str(value),

            font=font

        )

        text_width = bbox[2] - bbox[0]

        xx = x + (width - text_width) // 2

        self.text(

            xx,

            y,

            value,

            font,

            color

        )

    # =================================================

    def paste_image(

        self,

        image,

        x,

        y,

        width,

        height,

        keep_ratio=True

    ):

        if isinstance(

            image,

            str

        ):

            image = Image.open(

                image

            ).convert(

                "RGB"

            )

        else:

            image = image.copy()

        if keep_ratio:

            image.thumbnail(

                (

                    width,

                    height

                )

            )

        else:

            image = image.resize(

                (

                    width,

                    height

                )

            )

        offset_x = (

            width -

            image.width

        ) // 2

        offset_y = (

            height -

            image.height

        ) // 2

        self.image.paste(

            image,

            (

                x + offset_x,

                y + offset_y

            )

        )

    # =================================================

    def horizontal_progress(

        self,

        x,

        y,

        width,

        height,

        percentage,

        background=(230,230,230),

        foreground=theme.SECONDARY

    ):

        percentage = max(

            0,

            min(

                100,

                percentage

            )

        )

        self.rounded_box(

            x,

            y,

            width,

            height,

            fill=background,

            outline=background,

            radius=height//2,

            border_width=0

        )

        filled = int(

            width *

            percentage /

            100

        )

        if filled > 0:

            self.rounded_box(

                x,

                y,

                filled,

                height,

                fill=foreground,

                outline=foreground,

                radius=height//2,

                border_width=0

            )
