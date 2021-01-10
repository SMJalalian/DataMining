from sklearn.datasets import load_iris
from sklearn.preprocessing import MinMaxScaler
import numpy as np

X, y = load_iris(return_X_y=True)
scaler = MinMaxScaler()
scaler.fit(X)

X_scaled = scaler.transform(X)
# Manually normalise without using scikit-learn
X_manual_scaled = (X - X.min(axis=0)) / (X.max(axis=0) - X.min(axis=0))
# Verify manually VS scikit-learn estimation
print(np.allclose(X_scaled, X_manual_scaled))
#True


import matplotlib.pyplot as plt
fig, axes = plt.subplots(1,3)
axes[0].scatter(X[:,0], X[:,1], c=y)
axes[0].set_title("Original data")
axes[1].scatter(X_scaled[:,0], X_scaled[:,1], c=y)
axes[1].set_title("MinMax scaled data")
plt.show()