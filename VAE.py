# import torch
# import torch.nn as nn
# import torch.nn.functional as F
# import numpy as np
# import matplotlib.pyplot as plt

# from sklearn.datasets import load_digits
# from sklearn.model_selection import train_test_split
# from torch.utils.data import DataLoader,TensorDataset

# digits=load_digits()
# # print(f'x didgit shape before the float32/16.0{digits}')
# x=digits.images.astype(np.float32)/16.0
# # print(f'x didgit shape after the float32/16.0{x}')
# x=x.reshape(-1,64)

# x_train,x_test=train_test_split(x,test_size=0.2,random_state=42)

# train_data=TensorDataset(torch.from_numpy(x_train))
# train_loader=DataLoader(train_data,batch_size=64,shuffle=True)

# print("trainingData shape:",x_train.shape)

# class VAE(nn.Module):
    
#     def __init__(self, latent_dim=2):
#         super().__init__()

#         # TODO 1: Encoder layers
#         # 64 -> 128 -> 64
#         self.encoder = nn.Sequential(
#             # Write Linear and ReLU layers
#             nn.Linear(64,128),
#             nn.Relu(),
#             nn.Linear(128,64),
#             nn.Relu()
#         )
#         # self.decoder=nn.Sequential(
#         #     nn.Linear(latent_dim,64),
#         #     nn.ReLU(),
#         #     nn.Linear(64,128),
#         #     nn.ReLU(),
#         #     nn.Linear(128,64),
#         #     nn.Sigmoid()
            
#         # )

#         # TODO 2: Separate output layers
#         self.fc_mu = nn.Linear(64, latent_dim)
#         # mean that will take 64 feactuers from encoder  and predicts mean with dim =2
#         self.fc_logvar = nn.Linear(64, latent_dim)
#         # it is an variance predicts the log variance with dim =2

#         # TODO 3: Decoder layers
#         # latent_dim -> 64 -> 128 -> 64
#         self.decoder = nn.Sequential(
#             # Write Linear and ReLU layers
#             # Final layer should use Sigmoid
#             nn.Linear(64,128),
#             nn.ReLU(),
#             nn.Linear(128,64),
#             nn.Sigmoid()
#         )

#     def encode(self, x):
#         # TODO 4: Extract encoder features
#         # Return mu and logvar
#         h=self.encoder(x)
#         mu=self.fc_mu(h)
#         logvar=self.fc_logvar(h)
#         return mu,logvar

#     def reparameterize(self, mu, logvar):
#         # TODO 5: Calculate standard deviation
#         # Generate random epsilon
#         # Return z = mu + std * epsilon
#         std=torch.exp(0.5*logvar)
#         epsilion=torch.randn_like(std)
#         z=mu+std*epsilion
        
#         return z

#     def decode(self, z):
#         # TODO 6: Reconstruct the input
#         reconst=self.decoder(z)
#         return reconst
        

#     def forward(self, x):
#         # TODO 7: Connect encoder, sampling and decoder
#         # Return reconstruction, mu, logvar
#         mu,logvar=self.encoder(x)
#         z=self.reparameterize(mu,logvar)
#         reconstruction=self.decode(z)
#         return reconstruction,mu,logvar
    
#     def Vae_Loss(reconstruction,x,mu,logvar):
#         reconstraction_loss=F.binary_cross_entropy(
#             reconstruction,x,reduction=sum
#         )
#         """ reconstruction: the image predicted by your decoder.
#             x: the original image.
#                 reduction="sum": adds the loss across all pixels and samples in the batch."""
#         kl_loss=-0.5*torch.sum(1+logvar-mu.pow(2)-logvar.exp())
#         """ 
#         It encourages the latent distribution to remain close to a standard normal distribution, \(N(0,I)\).

# The terms represent:
# - mu.pow(2): squared mean.
# - logvar.exp(): variance, because logvar stores log variance.
# - 1 + logvar: remaining terms in the Gaussian KL formula."""
#         loss=reconstraction_loss+kl_loss
#         return loss
#     """ 
#     What happens during training?
# \[
# \boxed{\text{Total loss}=\text{Reconstruction loss}+\text{KL loss}}
# \]

# The reconstruction term teaches the decoder to generate recognizable digits. The KL term regularizes the latent space so you can sample latent vectors and generate new digits."""

# model=VAE(latent_dim=2)
# sample=torch.from_numpy(x_train[:4])
# reconstraction,mu,logvar=model(sample)
# print()
# print("Reconstruction:", reconstraction.shape)
# print("Mu:", mu.shape)
# print("Log variance:", logvar.shape)

"""
Variational Autoencoder (VAE) from scratch using PyTorch
Dataset: scikit-learn Digits (8x8 grayscale handwritten digits)
"""

import numpy as np
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import torch.nn.functional as F

from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from torch.utils.data import DataLoader, TensorDataset


# 1. Reproducibility and device
torch.manual_seed(42)
np.random.seed(42)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("Using device:", device)


# 2. Load and normalize the dataset
digits = load_digits()

# Original pixel values are integers from 0 to 16.
# Normalize to [0, 1], which matches the decoder's Sigmoid output.
x = digits.images.astype(np.float32) / 16.0

# Flatten every 8x8 image into 64 pixel values.
x = x.reshape(-1, 64)

# Keep 20% for testing; do not train on this held-out set.
x_train, x_test = train_test_split(
    x, test_size=0.2, random_state=42
)

# DataLoader provides shuffled mini-batches for training.
train_data = TensorDataset(torch.from_numpy(x_train))
train_loader = DataLoader(train_data, batch_size=64, shuffle=True)

print("Training data shape:", x_train.shape)
print("Test data shape:", x_test.shape)


# 3. Define the Variational Autoencoder
class VAE(nn.Module):
    def __init__(self, latent_dim=2):
        super().__init__()

        # Encoder: 64 input pixels -> 128 hidden units -> 64 features.
        self.encoder = nn.Sequential(
            nn.Linear(64, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU()
        )

        # Predict the latent Gaussian's mean and log variance.
        # Both output tensors have shape [batch_size, latent_dim].
        self.fc_mu = nn.Linear(64, latent_dim)
        self.fc_logvar = nn.Linear(64, latent_dim)

        # Decoder: latent vector -> 64 -> 128 -> 64 output pixels.
        # Sigmoid makes each reconstructed pixel lie in [0, 1].
        self.decoder = nn.Sequential(
            nn.Linear(latent_dim, 64),
            nn.ReLU(),
            nn.Linear(64, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.Sigmoid()
        )

    def encode(self, x):
        """Convert input images into latent mean and log variance."""
        features = self.encoder(x)
        mu = self.fc_mu(features)
        logvar = self.fc_logvar(features)
        return mu, logvar

    def reparameterize(self, mu, logvar):
        """
        Sample z = mu + std * epsilon, where epsilon ~ N(0, I).
        This formulation allows gradients to pass through mu and std.
        """
        std = torch.exp(0.5 * logvar)  # Convert log variance to std deviation.
        epsilon = torch.randn_like(std)  # Sample standard-normal noise.
        z = mu + std * epsilon
        return z

    def decode(self, z):
        """Reconstruct a 64-pixel image from a latent vector."""
        reconstruction = self.decoder(z)
        return reconstruction