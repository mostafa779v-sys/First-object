"""
====================================================
BrainVisionAI
Charts Engine
====================================================
"""

from . import theme


# ==================================================
# Base Chart
# ==================================================

class Chart:

    def __init__(

        self,

        canvas,

        x,

        y,

        width,

        height,

        title

    ):

        self.canvas = canvas

        self.x = x

        self.y = y

        self.width = width

        self.height = height

        self.title = title

    def draw_background(self):

        self.canvas.shadow_box(

            self.x,

            self.y,

            self.width,

            self.height

        )

        self.canvas.text(

            self.x + 25,

            self.y + 20,

            self.title,

            theme.HEADER_FONT,

            theme.PRIMARY

        )


# ==================================================
# Probability Bars
# ==================================================

class ProbabilityChart(Chart):

    def __init__(

        self,

        canvas,

        probabilities,

        x=1850,

        y=1350,

        width=1250,

        height=700

    ):

        super().__init__(

            canvas,

            x,

            y,

            width,

            height,

            "Prediction Probabilities"

        )

        self.probabilities = dict(

            sorted(

                probabilities.items(),

                key=lambda x: x[1],

                reverse=True

            )

        )

    # ==============================================

    def color(self, value):

        if value >= 90:

            return theme.SUCCESS

        elif value >= 70:

            return theme.SECONDARY

        elif value >= 40:

            return theme.WARNING

        else:

            return theme.DANGER

    # ==============================================

    def draw_background(self):

        self.canvas.shadow_box(

            self.x,

            self.y,

            self.width,

            self.height

        )

        self.canvas.text(

            self.x + 40,

            self.y + 35,

            self.title,

            theme.HEADER_FONT,

            theme.PRIMARY

        )

        self.canvas.line(

            self.x + 35,

            self.y + 95,

            self.x + self.width - 35,

            self.y + 95,

            theme.BORDER,

            2

        )

    # ==============================================

    def draw(self):

        self.draw_background()

        start_y = self.y + 150

        bar_width = 700

        bar_height = 32

        spacing = 110

        rank = 1

        for name, value in self.probabilities.items():

            color = self.color(value)

            self.canvas.text(

                self.x + 40,

                start_y,

                f"{rank}. {name.upper()}",

                theme.TEXT_FONT,

                theme.BLACK

            )

            self.canvas.horizontal_progress(

                self.x + 320,

                start_y + 5,

                bar_width,

                bar_height,

                value,

                foreground=color

            )

            self.canvas.text(

                self.x + 1070,

                start_y,

                f"{value:.2f}%",

                theme.TEXT_FONT,

                color

            )

            start_y += spacing
            rank += 1


# ==================================================
# Confidence Gauge
# ==================================================

class ConfidenceGauge(Chart):

    def __init__(

        self,

        canvas,

        confidence,

        x,

        y,

        width=300,

        height=170

    ):

        super().__init__(

            canvas,

            x,

            y,

            width,

            height,

            "Confidence Gauge"

        )

        self.confidence = confidence

    # ==============================================

    def draw(self):

        self.draw_background()

        color = ProbabilityChart.color(

            self,

            self.confidence

        )

        self.canvas.rounded_box(

            self.x + 25,

            self.y + 70,

            240,

            25,

            fill=(230,230,230),

            outline=(230,230,230)

        )

        filled = int(

            240 *

            self.confidence /

            100

        )

        self.canvas.rounded_box(

            self.x + 25,

            self.y + 70,

            filled,

            25,

            fill=color,

            outline=color

        )

        self.canvas.text(

            self.x + 95,

            self.y + 110,

            f"{self.confidence:.2f}%",

            theme.PERCENT_FONT,

            color

        )


# ==================================================
# Future Charts
# ==================================================

class PieChart(Chart):

    """
    Reserved for v1.0
    """

    pass


class RadarChart(Chart):

    """
    Reserved for v1.2
    """

    pass


class TrendChart(Chart):

    """
    Reserved for v2.0
    """

    pass
