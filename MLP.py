import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset
import numpy as np
import pandas as pd

X = df.iloc[:, :-1].values.astype(np.float32)
y = df.iloc[:, -1].values.astype(np.float32).reshape(-1, 1)

n = int(len(X)*0.8)
X_train, X_valid = X[:n], X[n:]
y_train, y_valid = y[:n], y[n:]

train_ds = TensorDataset(torch.tensor(X_train), torch_tensor(y_train))
valid_ds = TensorDataset(torch.tensor(X_valid), torch_tensor(y_valid))

train_loader = DataLoader(train_ds, batch_size=64, shuffle=True)
valid_loader = DataLoader(valid_ds, batch_size=128)

class MLP(nn.Module):
  def __init__(self, in_dim, hidden=[128, 64], out_dim=1):
    super().__init__()
    layers = []
    prev = in_dim
    for h in hidden:
      layers += [nn.Linear(prev, h), nn.ReLU(), nn.Dropout(0.2)]
      prev = h
    layers += [nn.Linear(prev, out_dim)]
    self.net = nn.Sequential(*layers)
  def forward(self, x):
    return self.net(x)

model = MLP(in_dim=X.shape[1], out_dim=1)

loss_fn = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

for epoch in range(20):
  model.train()
  total_loss = 0
  for xb, yb in train_loader:
    pred = model(xb)
    loss = loss_fn(pred, yb)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    total_loss += loss.item()
  val_loss = 0
  model.eval()
  with torch.no_grad():
    for xb, yb in valid_loader:
      val_loss += loss_fn(model(xb), yb).item()
  print(f"Epoch {epoch+1:02d} | Train Loss: {total_loss/len(train_loader}: 4f} | Val Loss: {val_loss/len(valid_loader):.4f}")


torch.save(model, 'mlp_model.pth')

model = torch.load('mlp_model.pth') #need definition of MLP class
model.eval()
