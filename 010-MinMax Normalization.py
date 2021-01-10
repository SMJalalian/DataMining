from sklearn.datasets import load_iris
from sklearn.preprocessing import MinMaxScaler
import numpy as np

X, y = load_iris(return_X_y=True)
scaler = MinMaxScaler()
scaler.fit(X)

X_scaled = scaler.transform(X)

X_manual_scaled = (X - X.min(axis=0)) / (X.max(axis=0) - X.min(axis=0))
#*********************************************************************** 
import matplotlib.pyplot as plt
fig, axes = plt.subplots(1,4)
axes[0].scatter(X[:,0], X[:,1], c=y)
axes[0].set_title("Sepal Original")
axes[1].scatter(X_scaled[:,0], X_scaled[:,1], c=y)
axes[1].set_title("Sepal Scaled")
axes[2].scatter(X[:,2], X[:,3], c=y)
axes[2].set_title("Petal Original")
axes[3].scatter(X_scaled[:,2], X_scaled[:,3], c=y)
axes[3].set_title("Petal Scaled")
plt.show()