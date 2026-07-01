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

        x=820,

        y=880,

        width=730,

        height=250

    ):

        super().__init__(

            canvas,

            x,

            y,

            width,

            height,

            "Class Probabilities"

        )

        self.probabilities = probabilities

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

    def progress_bar(

        self,

        x,

        y,

        width,

        percent,

        color

    ):

        self.canvas.rounded_box(

            x,

            y,

            width,

            22,

            fill=(235,235,235),

            outline=(235,235,235)

        )

        filled = int(

            width *

            percent /

            100

        )

        self.canvas.rounded_box(

            x,

            y,

            filled,

            22,

            fill=color,

            outline=color

        )

    # ==============================================

    def draw(self):

        self.draw_background()

        yy = self.y + 65

        for name, value in self.probabilities.items():

            color = self.color(value)

            self.canvas.text(

                self.x + 25,

                yy,

                name,

                theme.TEXT_FONT,

                theme.BLACK

            )

            self.progress_bar(

                self.x + 190,

                yy,

                360,

                value,

                color

            )

            self.canvas.text(

                self.x + 580,

                yy,

                f"{value:.2f}%",

                theme.TEXT_FONT,

                color

            )

            yy += 42


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
