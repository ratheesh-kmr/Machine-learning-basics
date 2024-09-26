import seaborn as sns
import numpy 
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error , r2_score

mydata = pd.read_csv("C:/Users/rathe/Downloads/Cars data set/car_price.csv")
mydata = pd.get_dummies(mydata,drop_first=True) #converts the dissimilar types to similar one 
print(mydata.head())

#drops the null values
mydata = mydata.dropna()

#handling missing values
mean_val = mydata['price'].mean()
mydata['price'].fillna(mean_val,inplace=True)
print(mydata['price'])

#separate the features and target value
x = mydata.drop('price',axis=1)
y = mydata['price']

#train the models

x_train , x_test , y_train ,y_test  = train_test_split(x,y,test_size=0.2,random_state=42)

#use regression methods
model = LinearRegression()
model.fit(x_train,y_train)
y_pred = model.predict(x_test)
print("Mean Square Error:",mean_squared_error(y_test,y_pred))
print("R^2 score",r2_score(y_test,y_pred))

#outlers
print(mydata.describe())

#plotting the outlers
plt.figure(figsize=(10, 6))
sns.boxplot(data=mydata['price'])
plt.title = "Car price dataset"
plt.show()


Q1 = mydata.quantile(0.25)
Q3 = mydata.quantile(0.75)
IQR = Q3 - Q1

# Identifying outliers
outliers = mydata[((mydata < (Q1 - 1.5 * IQR)) | (mydata > (Q3 + 1.5 * IQR))).any(axis=1)]
print(outliers)

#removing outlers
mydata_no_outliers = mydata[~((mydata < (Q1 - 1.5 * IQR)) | (mydata > (Q3 + 1.5 * IQR))).any(axis=1)]
print(mydata_no_outliers.describe())

plt.plot()
