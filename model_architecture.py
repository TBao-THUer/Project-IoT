import torch
import torch.nn as nn
from torchvision.models import mobilenet_v2
from torch.nn import functional as F

class Eye_model(nn.Module):
    def __init__(self, num_classes=2):
        super(Eye_model, self).__init__()

        # Load pretrained MobilenetV2 model
        self.base_model = mobilenet_v2(pretrained=True)
        out_features = self.base_model.classifier[1].out_features
        
        # Add custom layers
        self.head = nn.Sequential(
            nn.Flatten(),
            nn.Linear(out_features, 64),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(64, num_classes),
        )
        
        # Freeze base model layers
        for param in self.base_model.parameters():
            param.requires_grad = False

    def forward(self, inp):
        x = self.base_model(inp)
        if isinstance(x, tuple):
            x = x[0]
        return self.head(x)