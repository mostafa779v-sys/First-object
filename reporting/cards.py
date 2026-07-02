# ==========================================
# BrainVisionAI
# reporting/cards.py
# ==========================================

from PIL import ImageDraw, ImageFont
import textwrap


# ==========================================
# Colors
# ==========================================

CARD_BACKGROUND = (255, 255, 255)

CARD_BORDER = (220, 220, 220)

TITLE_COLOR = (35, 55, 85)

TEXT_COLOR = (45, 45, 45)

GREEN = (34, 170, 90)

YELLOW = (245, 180, 40)

RED = (215, 60, 60)

LIGHT_GRAY = (150, 150, 150)


# ==========================================
# Fonts
# ==========================================

try:

    FONT_TITLE = ImageFont.truetype(
        "DejaVuSans-Bold.ttf",
        34
    )

    FONT_SUBTITLE = ImageFont.truetype(
        "DejaVuSans-Bold.ttf",
        24
    )

    FONT_TEXT = ImageFont.truetype(
        "DejaVuSans.ttf",
        22
    )

    FONT_SMALL = ImageFont.truetype(
        "DejaVuSans.ttf",
        18
    )

except:

    FONT_TITLE = ImageFont.load_default()

    FONT_SUBTITLE = ImageFont.load_default()

    FONT_TEXT = ImageFont.load_default()

    FONT_SMALL = ImageFont.load_default()


# ==========================================
# Helper Functions
# ==========================================

def draw_card(
    draw,
    x,
    y,
    w,
    h
):
    """
    Draw white rounded card.
    """

    draw.rounded_rectangle(

        [x, y, x + w, y + h],

        radius=25,

        fill=CARD_BACKGROUND,

        outline=CARD_BORDER,

        width=3

    )


def risk_color(confidence):

    if confidence >= 95:

        return GREEN

    elif confidence >= 70:

        return YELLOW

    else:

        return RED


def risk_text(confidence):

    if confidence >= 95:

        return "VERY HIGH"

    elif confidence >= 70:

        return "HIGH"

    elif confidence >= 40:

        return "MODERATE"

    else:

        return "LOW"


def draw_multiline(

    draw,

    text,

    x,

    y,

    width,

    font,

    fill,

    line_spacing=8

):

    wrapped = textwrap.fill(

        text,

        width=width

    )

    draw.multiline_text(

        (x, y),

        wrapped,

        fill=fill,

        font=font,

        spacing=line_spacing

    )


# ==========================================
# Diagnosis Card
# ==========================================

def draw_diagnosis_card(

    draw,

    x,

    y,

    w,

    h,

    diagnosis,

    confidence

):

    draw_card(

        draw,

        x,

        y,

        w,

        h

    )

    padding = 35

    cx = x + padding

    cy = y + padding

    # -----------------------------
    # Title
    # -----------------------------

    draw.text(

        (cx, cy),

        "AI DIAGNOSIS",

        font=FONT_TITLE,

        fill=TITLE_COLOR

    )

    cy += 60

    # -----------------------------
    # Diagnosis
    # -----------------------------

    draw.text(

        (cx, cy),

        "Diagnosis",

        font=FONT_SUBTITLE,

        fill=LIGHT_GRAY

    )

    cy += 38

    draw.text(

        (cx, cy),

        diagnosis.upper(),

        font=FONT_TITLE,

        fill=risk_color(confidence)

    )

    cy += 65

    # -----------------------------
    # Confidence
    # -----------------------------

    draw.text(

        (cx, cy),

        "Model Confidence",

        font=FONT_SUBTITLE,

        fill=LIGHT_GRAY

    )

    draw.text(

        (x + w - 210, cy),

        f"{confidence:.2f}%",

        font=FONT_SUBTITLE,

        fill=TITLE_COLOR

    )

    cy += 50
        # -----------------------------
    # Progress Bar
    # -----------------------------

    bar_x = cx

    bar_y = cy

    bar_w = w - (padding * 2)

    bar_h = 26

    draw.rounded_rectangle(

        (

            bar_x,
            bar_y,
            bar_x + bar_w,
            bar_y + bar_h

        ),

        radius=13,

        fill=(235,235,235)

    )

    filled = int(

        bar_w *

        confidence /

        100

    )

    draw.rounded_rectangle(

        (

            bar_x,
            bar_y,
            bar_x + filled,
            bar_y + bar_h

        ),

        radius=13,

        fill=risk_color(confidence)

    )

    cy += 55


    # -----------------------------
    # Risk Level
    # -----------------------------

    draw.text(

        (cx, cy),

        "Prediction Reliability",

        font=FONT_SUBTITLE,

        fill=LIGHT_GRAY

    )

    draw.text(

        (

            x + w - 250,

            cy

        ),

        risk_text(confidence),

        font=FONT_SUBTITLE,

        fill=risk_color(confidence)

    )

    cy += 60


    # -----------------------------
    # Separator
    # -----------------------------

    draw.line(

        (

            cx,

            cy,

            x + w - padding,

            cy

        ),

        fill=CARD_BORDER,

        width=2

    )

    cy += 30

    

    # -----------------------------
    # AI Explanation
    # -----------------------------

    draw.text(

        (cx, cy),

        "AI Explanation",

        font=FONT_SUBTITLE,

        fill=TITLE_COLOR

    )

    cy += 40


    explanation = (

        "The neural network detected image "

        "features that are highly consistent "

        f"with {diagnosis}. "

        "The highlighted Grad-CAM region "

        "shows the area that contributed "

        "most strongly to the final "

        "prediction."

    )

    draw_multiline(

        draw,

        explanation,

        cx,

        cy,

        width=42,

        font=FONT_TEXT,

        fill=TEXT_COLOR,

        line_spacing=10

    )

    cy += 165


     # -----------------------------
    # Clinical Recommendation
    # -----------------------------

    draw.text(

        (cx, cy),

        "Clinical Recommendation",

        font=FONT_SUBTITLE,

        fill=TITLE_COLOR

    )

    cy += 38

    recommendation = (

        "This AI result is intended to "

        "assist clinical decision-making "

        "and should always be interpreted "

        "together with MRI findings and "

        "radiologist assessment."

    )

    draw_multiline(

        draw,

        recommendation,

        cx,

        cy,

        width=42,

        font=FONT_SMALL,

        fill=(90, 90, 90),

        line_spacing=8

    )

    cy += 120

    # -----------------------------
    # AI Summary
    # -----------------------------

    draw.text(

        (cx, cy),

        "Summary",

        font=FONT_SUBTITLE,

        fill=TITLE_COLOR

    )

    cy += 42

    summary = (

        f"The AI model classified this MRI as "

        f"{diagnosis.upper()} with a confidence "

        f"of {confidence:.2f}%. "

        "The highlighted Grad-CAM region "

        "indicates where the neural network "

        "focused most strongly during the "

        "decision-making process."

    )

    draw_multiline(

        draw,

        summary,

        cx,

        cy,

        width=42,

        font=FONT_TEXT,

        fill=TEXT_COLOR,

        line_spacing=10

    )

    cy += 150

    # -----------------------------
    # Disclaimer
    # -----------------------------

    draw.line(

        (

            cx,

            cy,

            x + w - padding,

            cy

        ),

        fill=CARD_BORDER,

        width=2

    )

    cy += 25

    draw.text(

        (cx, cy),

        "Disclaimer",

        font=FONT_SUBTITLE,

        fill=TITLE_COLOR

    )

    cy += 38

    disclaimer = (

        "BrainVisionAI is an AI-assisted "

        "decision support system. "

        "The generated diagnosis should "

        "not replace professional medical "

        "judgment or radiological reporting."

    )

    draw_multiline(

        draw,

        disclaimer,

        cx,

        cy,

        width=42,

        font=FONT_SMALL,

        fill=(120, 120, 120),

        line_spacing=8

    )

    cy += 105

    # -----------------------------
    # Report Status
    # -----------------------------

    draw.line(

        (

            cx,

            cy,

            x + w - padding,

            cy

        ),

        fill=CARD_BORDER,

        width=2

    )

    cy += 28

    draw.text(

        (cx, cy),

        "Report Status",

        font=FONT_SUBTITLE,

        fill=TITLE_COLOR

    )

    draw.text(

        (

            x + w - 180,

            cy

        ),

        "COMPLETED",

        font=FONT_SUBTITLE,

        fill=GREEN

    )

    cy += 45

    draw.text(

        (cx, cy),

        "Generated automatically by BrainVisionAI.",

        font=FONT_SMALL,

        fill=LIGHT_GRAY

    )   
# =====================================================
# Diagnosis Card Wrapper
# =====================================================

class DiagnosisCard:

    def __init__(

        self,

        canvas,

        diagnosis,

        confidence,

        x=1850,

        y=230,

        width=1250,

        height=1050

    ):

        self.canvas = canvas

        self.diagnosis = diagnosis

        self.confidence = confidence

        self.x = x

        self.y = y

        self.width = width

        self.height = height

    # =================================================

    def draw(self):

        draw_diagnosis_card(

            self.canvas.draw,

            self.x,

            self.y,

            self.width,

            self.height,

            self.diagnosis,

            self.confidence

        )
