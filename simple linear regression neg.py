import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

df=pd.read_csv("Machine Learning/car_dealer.csv")
model=LinearRegression()
x=df['car age'].values.reshape(-1,1) #here arrays are converted to numpy series from pandas
#x=df[['car age']] #here arrays are in pandas
y=df['price']
model.fit(x,y)
plt.figure(figsize=(10,6)) #given a figure size
#plt.scatter(x,y,color='blue',label='Data points')  #showed only the points, scatter is a kind of plot nad generally fetches all the
# - cordinates from x and y array
for i in range(len(df)):
    plt.scatter(x[i],y[i]) #x.iloc[i] is used when using pandas
    plt.text(x[i],y[i],[i+1]) 

plt.plot(x, model.predict(x), color='red', linewidth=2, label='Linear regression') # showed the regression line, x wrt y here
plt.xlabel('Car Age')
plt.ylabel('Price')
# plt.legend() #shows legend
# plt.grid(True) #displays grid
plt.show()


prec_value=11
new_price=model.predict([[prec_value]])
print(f'Predicted price for a car of age {prec_value}: {new_price[0]}')