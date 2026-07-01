"""
====================================================
BrainVisionAI
Report Builder
====================================================
"""

from .canvas import ReportCanvas

from .header import Header

from .footer import Footer

from .images import MRISection

from .cards import (

    DiagnosisCard,

    ConfidenceCard,

    InfoCard

)

from .charts import (

    ProbabilityChart,

    ConfidenceGauge

)

from .metadata import MetadataSection


class ReportBuilder:

    """
    Main Report Builder
    """

    def __init__(

        self,

        original_image,

        gradcam_image,

        diagnosis,

        confidence,

        probabilities,

        model_name,

        version,

        device,

        image_size

    ):

        self.canvas = ReportCanvas()

        self.original_image = original_image

        self.gradcam_image = gradcam_image

        self.diagnosis = diagnosis

        self.confidence = confidence

        self.probabilities = probabilities

        self.model_name = model_name

        self.version = version

        self.device = device

        self.image_size = image_size

    # ==================================================

    def draw_header(self):

        Header(

            self.canvas,

            self.version

        ).draw()

    # ==================================================

    def draw_images(self):

        MRISection(

            self.canvas,

            self.original_image,

            self.gradcam_image

        ).draw()

    # ==================================================

    def draw_cards(self):

        DiagnosisCard(

            self.canvas,

            self.diagnosis,

            self.confidence

        ).draw()

    # ==================================================

    def draw_charts(self):

        ProbabilityChart(

            self.canvas,

            self.probabilities

        ).draw()

    # ==================================================

    def draw_metadata(self):

        MetadataSection(

            self.canvas,

            self.model_name,

            self.version,

            self.device,

            self.image_size

        ).draw()

    # ==================================================

    def draw_footer(self):

        Footer(

            self.canvas,

            self.model_name

        ).draw()

    # ==================================================

    def build(self):

        self.draw_header()

        self.draw_images()

        self.draw_cards()

        self.draw_charts()

        self.draw_metadata()

        self.draw_footer()

    # ==================================================

    def save(

        self,

        path

    ):

        self.canvas.save(path)
