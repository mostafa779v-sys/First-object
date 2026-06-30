import torch

# ==========================
# Device
# ==========================

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# ==========================
# Image Settings
# ==========================

IMAGE_SIZE = 224
NUM_CLASSES = 4

CLASS_NAMES = [
    "glioma",
    "meningioma",
    "notumor",
    "pituitary"
]

# ==========================
# Paths
# ==========================

MODEL_PATH = "../models/BrainVisionAI_v1.pth"
