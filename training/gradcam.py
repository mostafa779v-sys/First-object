import os
import cv2
import numpy as np

from torchvision import transforms
from pytorch_grad_cam import GradCAM
from pytorch_grad_cam.utils.image import show_cam_on_image

from config import IMAGE_SIZE, DEVICE
from utils import load_image


transform = transforms.Compose([
    transforms.Resize((IMAGE_SIZE, IMAGE_SIZE)),
    transforms.ToTensor(),
])


def generate_gradcam(model, image_path, save_path="../results/gradcam_result.jpg"):

    image = load_image(image_path)

    rgb_image = np.array(
        image.resize((IMAGE_SIZE, IMAGE_SIZE))
    ).astype(np.float32) / 255.0

    input_tensor = transform(image).unsqueeze(0).to(DEVICE)

    target_layers = [model.blocks[-1]]

    cam = GradCAM(
        model=model,
        target_layers=target_layers
    )

    grayscale_cam = cam(input_tensor=input_tensor)[0]

    result = show_cam_on_image(
        rgb_image,
        grayscale_cam,
        use_rgb=True
    )

    os.makedirs(
        os.path.dirname(save_path),
        exist_ok=True
    )

    cv2.imwrite(
        save_path,
        cv2.cvtColor(result, cv2.COLOR_RGB2BGR)
    )

    return save_path
