import matplotlib.pyplot as plt
import pandas as pd

# Load the data
mydata = pd.read_csv("C:/Users/rathe/Downloads/Cars data set/car_price.csv")

# Plotting histogram of car prices
x = mydata['price']
plt.hist(x, bins=30, edgecolor='k', alpha=0.7)
plt.title('Car Price Distribution')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.show()

# Bivariate analysis using hexbin
x = mydata['cylindernumber'].astype('category').cat.codes  # Convert categorical to numerical
y = mydata['price']
plt.hexbin(x, y, gridsize=50, cmap='Blues')
plt.colorbar(label='Count')
plt.xlabel('Cylinder Number')
plt.ylabel('Price')
plt.title('Hexbin plot of Cylinder Number vs Price')
plt.show()
