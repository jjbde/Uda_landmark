import torch
import torch.nn as nn


# define the CNN architecture
class MyModel(nn.Module):
    def __init__(self, num_classes: int = 1000, dropout: float = 0.7) -> None:

        super().__init__()

        # YOUR CODE HERE
        # Define a CNN architecture. Remember to use the variable num_classes
        # to size appropriately the output of your classifier, and if you use
        # the Dropout layer, use the variable "dropout" to indicate how much
        # to use (like nn.Dropout(p=dropout))
        
        self.model = nn.Sequential(
            nn.Conv2d(in_channels=3, out_channels=16, kernel_size=3, padding=1),
            #nn.BatchNorm2d(16),   BatchNorm is not to be introduced to raw data/ the input layer to the CNN, only in subsequent layers
            nn.MaxPool2d(2, 2),
            #nn.Dropout(p=dropout),
            nn.ReLU(),
            
            nn.Conv2d(16, 32, 3, padding=1),  # -> 32x112x112
            nn.BatchNorm2d(32),
            nn.MaxPool2d(2, 2),  # -> 32x56x56
            nn.ReLU(),
           nn.Dropout(p=dropout),
            
            
            
            nn.Conv2d(32, 64, 3, padding=1),  # -> 64x56x56
            nn.BatchNorm2d(64),
            nn.MaxPool2d(2, 2),  # -> 64x28x28
            nn.ReLU(),
            nn.Dropout(p=dropout),
            
            
            
            nn.Conv2d(64, 128, 3, padding=1),  # -> 128x28x28
            nn.BatchNorm2d(128),
            nn.MaxPool2d(2, 2),  # -> 128x14x14
            nn.ReLU(),
            nn.Dropout(p=dropout),
            
            
            #nn.Conv2d(128, 256, 3, padding=1),  # -> 256x14x14
           # nn.BatchNorm2d(256),
           # nn.MaxPool2d(2, 2),  # -> 256x7x7
           # nn.ReLU(),
            #nn.Dropout(p=dropout),
            
            
           # nn.Flatten(),  # -> 1x256x7x7
            #nn.Linear(256 * 7 * 7, 4000),  # -> 4000
           # nn.BatchNorm1d(4000),
           # nn.ReLU(),
           # nn.Dropout(p=dropout),
            #nn.Linear(4000, 1024),
            #nn.BatchNorm1d(1024),
            #nn.ReLU(),
            #nn.Dropout(p=dropout),
            #nn.Linear(1024, 512),
            #nn.BatchNorm1d(512),
            #nn.ReLU(),
            #nn.Dropout(p=dropout),
            #nn.Linear(512, num_classes)
           # nn.Linear(4000, num_classes)
            
            
            
            
            nn.Flatten(),  # -> 1x128x14x14
            nn.Linear(128 * 14 * 14, 6400),  # -> 6400
            nn.Dropout(p=dropout),
            nn.ReLU(),
            
            nn.Linear(6400, 1600),
            nn.BatchNorm1d(1600),
            nn.ReLU(),
            nn.Dropout(p=dropout),
            
            nn.Linear(1600, 400),
            nn.BatchNorm1d(400),
            nn.ReLU(),
            nn.Dropout(p=dropout),
            
            nn.Linear(400, num_classes)
        
         
            
            
            
        )
        
        

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # YOUR CODE HERE: process the input tensor through the
        # feature extractor, the pooling and the final linear
        # layers (if appropriate for the architecture chosen)
        return self.model(x)
        #return x


######################################################################################
#                                     TESTS
######################################################################################
import pytest


@pytest.fixture(scope="session")
def data_loaders():
    from .data import get_data_loaders

    return get_data_loaders(batch_size=2)


def test_model_construction(data_loaders):

    model = MyModel(num_classes=23, dropout=0.3)

    dataiter = iter(data_loaders["train"])
    images, labels = dataiter.next()

    out = model(images)

    assert isinstance(
        out, torch.Tensor
    ), "The output of the .forward method should be a Tensor of size ([batch_size], [n_classes])"

    assert out.shape == torch.Size(
        [2, 23]
    ), f"Expected an output tensor of size (2, 23), got {out.shape}"
