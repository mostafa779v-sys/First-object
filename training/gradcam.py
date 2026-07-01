import cv2
import numpy as np
import torch

from PIL import Image
from torchvision import transforms

from pytorch_grad_cam import GradCAM
from pytorch_grad_cam.utils.image import show_cam_on_image

from config import IMAGE_SIZE, DEVICE
from utils import load_image


transform = transforms.Compose([
    transforms.Resize((IMAGE_SIZE, IMAGE_SIZE)),
    transforms.ToTensor(),
])


def generate_gradcam(model, image_path):

    image = load_image(image_path)

    rgb = np.array(image.resize((IMAGE_SIZE, IMAGE_SIZE))) / 255.0

    input_tensor = transform(image).unsqueeze(0).to(DEVICE)

    target_layer = model.blocks[-1]

    cam = GradCAM(
        model=model,
        target_layers=[target_layer]
    )

    grayscale_cam = cam(input_tensor=input_tensor)[0]

    visualization = show_cam_on_image(
        rgb,
        grayscale_cam,
        use_rgb=True
    )

    visualization = cv2.cvtColor(
        visualization,
        cv2.COLOR_RGB2BGR
    )

    return visualization
