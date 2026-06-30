from config import *
from model import create_model


def print_header():
    print("=" * 50)
    print("🧠 BrainVisionAI v0.1")
    print("=" * 50)


def show_system_info():
    print(f"Device      : {DEVICE}")
    print(f"Image Size  : {IMAGE_SIZE}")
    print(f"Classes     : {len(CLASS_NAMES)}")
    print()


def load_model():
    print("Loading Model...")

    model = create_model().to(DEVICE)

    print("✅ Model Loaded Successfully!\n")

    return model


def show_menu():
    print("Choose an option:")
    print("1 - Train Model")
    print("2 - Evaluate Model")
    print("3 - Predict MRI")
    print("4 - Exit")


def handle_choice(choice):

    if choice == "1":
        print("\n🚧 Training module is under development.")

    elif choice == "2":
        print("\n🚧 Evaluation module is under development.")

    elif choice == "3":
        print("\n🚧 Prediction module is under development.")

    elif choice == "4":
        print("\nGoodbye!")

    else:
        print("\n❌ Invalid choice.")


def main():

    print_header()

    show_system_info()

    model = load_model()

    show_menu()

    choice = input("\nEnter your choice: ")

    handle_choice(choice)


if __name__ == "__main__":
    main()
