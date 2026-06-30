import os

from config import *
from model import create_model
from predict import predict_image
from utils import (
    load_model_weights,
    print_success,
    print_error,
    print_line,
)


def print_header():

    print_line()
    print("🧠 BrainVisionAI v0.2")
    print_line()

    print(f"Device      : {DEVICE}")
    print(f"Image Size  : {IMAGE_SIZE}")
    print(f"Classes     : {CLASS_NAMES}")

    print_line()


def load_ai():

    print("\nLoading AI Model...\n")

    model = create_model()

    model = load_model_weights(
        model,
        MODEL_PATH,
        DEVICE
    )

    print_success("BrainVisionAI Ready!")

    return model


def predict_menu(model):

    image_path = input("\nEnter MRI image path:\n\n")

    if not os.path.exists(image_path):

        print_error("Image not found.")
        return

    print("\nAnalyzing MRI...\n")

    prediction, confidence, probabilities = predict_image(
        model,
        image_path
    )

    print_line()

    print(f"Prediction : {prediction}")

    print(f"Confidence : {confidence:.2f}%")

    print_line()

    print("\nAll Probabilities:\n")

    for name, value in probabilities.items():

        print(f"{name:12} : {value:.2f}%")

    print_line()


def main():

    print_header()

    model = load_ai()

    while True:

        print("\nChoose an option:\n")

        print("1 - Train Model")

        print("2 - Evaluate Model")

        print("3 - Predict MRI")

        print("4 - Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            print("\nTraining module coming soon.")

        elif choice == "2":

            print("\nEvaluation module coming soon.")

        elif choice == "3":

            predict_menu(model)

        elif choice == "4":

            print("\nGoodbye 👋")

            break

        else:

            print_error("Invalid choice.")


if __name__ == "__main__":

    main()
