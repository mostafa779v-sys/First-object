from config import *
from model import create_model
from predict import predict_image
from utils import (
    print_success,
    print_error,
    load_model_weights
)

import os


def print_header():
    print("=" * 50)
    print("🧠 BrainVisionAI v1.0")
    print("=" * 50)


def show_system_info():
    print(f"Device      : {DEVICE}")
    print(f"Image Size  : {IMAGE_SIZE}")
    print(f"Classes     : {len(CLASS_NAMES)}")
    print()


def load_ai_model():

    print("Loading AI Model...")

    model = create_model().to(DEVICE)

    if os.path.exists(MODEL_PATH):

        model = load_model_weights(
            model,
            MODEL_PATH,
            DEVICE
        )

        print_success("BrainVisionAI Ready!")

    else:

        print_error("Model not found!")
        return None

    return model


def predict_menu(model):

    image_path = input("\nEnter MRI image path: ")

    if not os.path.exists(image_path):

        print_error("Image not found!")
        return

    print("\nAnalyzing MRI...\n")

    prediction, confidence = predict_image(
        model,
        image_path
    )

    print("=" * 50)
    print(f"Prediction : {prediction}")
    print(f"Confidence : {confidence:.2f}%")
    print("=" * 50)


def main():

    print_header()

    show_system_info()

    model = load_ai_model()

    if model is None:
        return

    while True:

        print("\nChoose an option:")
        print("1 - Train Model")
        print("2 - Evaluate Model")
        print("3 - Predict MRI")
        print("4 - Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            print("\n🚧 Training module coming soon.")

        elif choice == "2":

            print("\n🚧 Evaluation module coming soon.")

        elif choice == "3":

            predict_menu(model)

        elif choice == "4":

            print("\nGoodbye 👋")
            break

        else:

            print_error("Invalid choice.")


if __name__ == "__main__":
    main()
