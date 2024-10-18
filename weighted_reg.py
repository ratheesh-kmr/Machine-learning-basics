import numpy as np
import matplotlib.pyplot as plt

# Gaussian Kernel function for weights
def gaussian_kernel(x, x_query, tau):
    return np.exp(-(x - x_query) ** 2 / (2 * tau ** 2))

# Locally Weighted Regression function
def locally_weighted_regression(x_train, y_train, x_query, tau):
    m = len(x_train)
    W = np.array([gaussian_kernel(x_train[i], x_query, tau) for i in range(m)])
    X_train = np.vstack((np.ones(m), x_train)).T
    theta = np.linalg.pinv(X_train.T @ (W[:, None] * X_train)) @ X_train.T @ (W * y_train)
    return np.array([1, x_query]) @ theta

# Generate a synthetic dataset
np.random.seed(0)
x_train = np.linspace(0, 10, 100)
y_train = np.sin(x_train) + np.random.randn(100) * 0.2  # Adding some noise

# Fit LWR model and make predictions
tau = 0.5  # Bandwidth parameter
x_query = np.linspace(0, 10, 100)
y_pred = np.array([locally_weighted_regression(x_train, y_train, x, tau) for x in x_query])

# Plotting the results
plt.figure(figsize=(10, 6))
plt.scatter(x_train, y_train, label="Data points", color="red")
plt.plot(x_query, y_pred, label="LWR prediction", color="blue")
plt.xlabel("x")
plt.ylabel("y")
plt.title(f"Locally Weighted Regression with tau={tau}")
plt.legend()
plt.show()
