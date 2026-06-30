from config import *
from model import create_model

def print_header():
    print("=" * 50)
    print("🧠 BrainVisionAI v0.1")
    print("=" * 50)

def system_info():
    print(f"Device      : {DEVICE}")
    print(f"Image Size  : {IMAGE_SIZE}")
    print(f"Classes     : {len(CLASS_NAMES)}")
    print()

def menu():
    print("Choose an option:")
    print("1 - Train Model")
    print("2 - Evaluate Model")
    print("3 - Predict MRI")
    print("4 - Exit")

def main():

    print_header()

    system_info()

    print("Loading Model...")

    model = create_model().to(DEVICE)

    print("✅ Model Loaded Successfully!\n")

    menu()

if __name__ == "__main__":
    main()
