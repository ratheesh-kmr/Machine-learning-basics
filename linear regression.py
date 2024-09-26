import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("Machine Learning/e_com_website.csv")

# Separate the features and the target
X = data[['monthly sales']]
y = data['online ads']      

# Create the regression model
model = LinearRegression()

# Fit the model with the data
model.fit(X, y)

# Get the coefficients
slope = model.coef_[0]
intercept = model.intercept_

# Print the equation of the line
print(f"Equation of the line: y = {slope:.2f} * x + {intercept:.2f}")

# Plot the data points with store identification
plt.figure(figsize=(10, 6))
for i in range(len(data)):
    plt.scatter(X.iloc[i], y.iloc[i], label=data['Online store'][i])
    plt.text(X.iloc[i],y.iloc[i], data['Online store'][i])

# Plot the regression line
plt.plot(X, model.predict(X), color='red', linewidth=2)

# Add labels and title
plt.xlabel('Monthly Sales')
plt.ylabel('Online Ads')
plt.title('Monthly Sales vs Online Ads')

# Show legend
plt.legend(loc='upper left')

# Show the plot
plt.show()

# Predicting for a new value
prec_value = 2000
predicted_sales = model.predict([[prec_value]])  # Pass as a nested list or 2D array

print(f'Predicted sales for an online ad cost of {prec_value}: {predicted_sales[0]}')
