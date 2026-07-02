"""
====================================================
BrainVisionAI
Professional Header
====================================================
"""

from datetime import datetime

from . import theme


class Header:

    def __init__(

        self,

        canvas,

        version="v0.6"

    ):

        self.canvas = canvas

        self.version = version

    # =====================================================

    def draw(self):

        # ==========================================
        # Background
        # ==========================================

        self.canvas.rectangle(

            0,

            0,

            theme.PAGE_WIDTH,

            theme.HEADER_HEIGHT,

            theme.PRIMARY

        )

        # ==========================================
        # Logo
        # ==========================================

        self.canvas.text(

            80,

            45,

            "🧠",

            theme.BIG_FONT,

            theme.WHITE

        )

        # ==========================================
        # Product Name
        # ==========================================

        self.canvas.text(

            170,

            40,

            "BrainVisionAI",

            theme.TITLE_FONT,

            theme.WHITE

        )

        self.canvas.text(

            175,

            108,

            "Artificial Intelligence MRI Analysis System",

            theme.SMALL_FONT,

            (230,230,230)

        )

        # ==========================================
        # Right Side
        # ==========================================

        right = theme.PAGE_WIDTH - 650

        self.canvas.text(

            right,

            42,

            "MRI Diagnostic Report",

            theme.HEADER_FONT,

            theme.WHITE

        )

        self.canvas.text(

            right,

            102,

            f"Software Version : {self.version}",

            theme.SMALL_FONT,

            theme.WHITE

        )

        self.canvas.text(

            right,

            138,

            datetime.now().strftime(

                "%Y-%m-%d %H:%M"

            ),

            theme.SMALL_FONT,

            theme.WHITE

        )

        # ==========================================
        # Bottom Line
        # ==========================================

        self.canvas.line(

            0,

            theme.HEADER_HEIGHT,

            theme.PAGE_WIDTH,

            theme.HEADER_HEIGHT,

            theme.SECONDARY,

            6

        )
