from config import *
from model import create_model

def main():

    print("="*40)
    print("BrainVisionAI")
    print("="*40)

    print(f"Device: {DEVICE}")
    print(f"Image Size: {IMAGE_SIZE}")
    print(f"Classes: {CLASS_NAMES}")

    model = create_model()

    print("\nModel Loaded Successfully!")

if __name__ == "__main__":
    main()
