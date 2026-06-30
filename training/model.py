import timm
import torch.nn as nn

from config import NUM_CLASSES


def create_model():

    model = timm.create_model(
        "efficientnet_b0",
        pretrained=True
    )

    model.classifier = nn.Sequential(
        nn.Dropout(0.2),
        nn.Linear(
            model.classifier.in_features,
            NUM_CLASSES
        )
    )

    return model
