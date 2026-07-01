import torch

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

from config import DEVICE, CLASS_NAMES


def evaluate(model, test_loader):

    """
    Evaluate trained model on test dataset.
    """

    model.eval()

    y_true = []
    y_pred = []

    with torch.no_grad():

        for images, labels in test_loader:

            images = images.to(DEVICE)
            labels = labels.to(DEVICE)

            outputs = model(images)

            _, predicted = torch.max(outputs, 1)

            y_true.extend(labels.cpu().numpy())
            y_pred.extend(predicted.cpu().numpy())

    accuracy = accuracy_score(
        y_true,
        y_pred
    )

    print("\n" + "=" * 50)
    print("🧠 BrainVisionAI Evaluation")
    print("=" * 50)

    print(f"\nOverall Accuracy : {accuracy*100:.2f}%")

    print("\nClassification Report\n")

    print(
        classification_report(
            y_true,
            y_pred,
            target_names=CLASS_NAMES,
            digits=4
        )
    )

    cm = confusion_matrix(
        y_true,
        y_pred
    )

    return accuracy, cm
