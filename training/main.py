from config import *
from model import create_model
from utils import (
    print_success,
    print_error,
    load_model_weights,
)
import os


def print_header():
    print("=" * 50)
    print("🧠 BrainVisionAI v0.2")
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

        print_error("Trained model not found!")

    return model


def show_menu():

    print("\nChoose an option:")

    print("1 - Train Model")

    print("2 - Evaluate Model")

    print("3 - Predict MRI")

    print("4 - Exit")


def handle_choice():

    choice = input("\nEnter your choice: ")

    if choice == "1":

        print("\n🚧 Training module is coming soon.")

    elif choice == "2":

        print("\n🚧 Evaluation module is coming soon.")

    elif choice == "3":

        print("\n🚧 Prediction module will be connected next.")

    elif choice == "4":

        print("\nGoodbye!")

    else:

        print_error("Invalid choice.")


def main():

    print_header()

    show_system_info()

    load_ai_model()

    show_menu()

    handle_choice()


if __name__ == "__main__":
    main()
