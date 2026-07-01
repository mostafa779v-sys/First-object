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

# ==========================
# Training Settings
# ==========================

BATCH_SIZE = 32
LEARNING_RATE = 0.001
EPOCHS = 10

# ==========================
# Dataset Paths
# ==========================

DATASET_PATH = "/kaggle/input/brain-tumor-mri-dataset"

TRAIN_PATH = DATASET_PATH + "/Training"
TEST_PATH = DATASET_PATH + "/Testing"
