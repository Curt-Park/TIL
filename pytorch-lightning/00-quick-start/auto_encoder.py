"""Auto-Encoder for quick-start.

Ref:
    https://pytorch-lightning.readthedocs.io/en/latest/starter/introduction.html

Visualize training:
    $ tensorboard --logdir .
    # open your browser to http://localhost:6006/
"""

import os
from torch import optim, nn, utils, Tensor, Generator
from torchvision.datasets import MNIST
from torchvision.transforms import ToTensor
from typing import Tuple
import pytorch_lightning as pl


# define the LightningModule
class LitAutoEncoder(pl.LightningModule):

    def __init__(self, encoder: nn.Module, decoder: nn.Module) -> None:
        """Init the auto-encoder."""
        super().__init__()
        self.encoder = encoder
        self.decoder = decoder

    def training_step(self, batch: Tuple[Tensor, Tensor], batch_idx: int) -> Tensor:
        """Define a training step for the train loop."""
        x, y = batch
        x = x.view(x.size(0), -1)
        z = self.encoder(x)
        x_hat = self.decoder(z)
        loss = nn.functional.mse_loss(x_hat, x)
        # Logging to TensorBoard by default
        self.log("train_loss", loss)
        return loss

    def validation_step(self, batch: Tuple[Tensor, Tensor], batch_idx: int) -> None:
        """Define a validation step for the validation loop."""
        x, y = batch
        x = x.view(x.size(0), -1)
        z = self.encoder(x)
        x_hat = self.decoder(z)
        test_loss = nn.functional.mse_loss(x_hat, x)
        self.log("val_loss", test_loss)

    def test_step(self, batch: Tuple[Tensor, Tensor], batch_idx: int) -> None:
        """Define a test step for the test loop."""
        # this is the test loop
        x, y = batch
        x = x.view(x.size(0), -1)
        z = self.encoder(x)
        x_hat = self.decoder(z)
        test_loss = nn.functional.mse_loss(x_hat, x)
        self.log("test_loss", test_loss)

    def configure_optimizers(self) -> optim.Optimizer:
        """Get the optimizer."""
        optimizer = optim.Adam(self.parameters(), lr=1e-3)
        return optimizer


if __name__ == "__main__":
    # init the autoencoder
    encoder = nn.Sequential(nn.Linear(28 * 28, 64), nn.ReLU(), nn.Linear(64, 3))
    decoder = nn.Sequential(nn.Linear(3, 64), nn.ReLU(), nn.Linear(64, 28 * 28))
    autoencoder = LitAutoEncoder(encoder, decoder)

    # setup data
    # Lightning supports ANY iterable (DataLoader, numpy, etc…) for the train/val/test/predict splits.
    train_set = MNIST(os.getcwd(), download=True, train=True, transform=ToTensor())
    train_set_size = int(len(train_set) * 0.8)  # use 20% of training data for validation
    valid_set_size = len(train_set) - train_set_size
    # split the train set into two
    train_set, valid_set = utils.data.random_split(
        train_set, [train_set_size, valid_set_size], generator=Generator().manual_seed(42)
    )
    train_loader = utils.data.DataLoader(train_set, num_workers=os.cpu_count())
    valid_loader = utils.data.DataLoader(valid_set, num_workers=os.cpu_count())

    # test set
    test_set = MNIST(os.getcwd(), download=True, train=False, transform=ToTensor())
    test_loader = utils.data.DataLoader(test_set, num_workers=os.cpu_count())

    # train the model (hint: here are some helpful Trainer arguments for rapid idea iteration)
    trainer = pl.Trainer(limit_train_batches=0.2, max_epochs=10)
    trainer.fit(autoencoder, train_loader, valid_loader)
    trainer.test(autoencoder, dataloaders=test_loader)

    # load checkpoint
    checkpoint = "./lightning_logs/version_0/checkpoints/epoch=0-step=100.ckpt"
    autoencoder = LitAutoEncoder.load_from_checkpoint(checkpoint, encoder=encoder, decoder=decoder)

    # choose your trained nn.Module
    encoder = autoencoder.encoder
    encoder.eval()

    # embed 4 fake images!
    fake_image_batch = Tensor(4, 28 * 28)
    embeddings = encoder(fake_image_batch)
    print("⚡" * 20, "\nPredictions (4 image embeddings):\n", embeddings, "\n", "⚡" * 20)
