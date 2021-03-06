# -*- coding: utf-8 -*-
"""Boston house price-Linear Regression model.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CBGpxzzD4aQYnxRyzTZCHcXcRHJ-wcI-

## **Linear Regression** Problem Solving
We are going to import our all libraries and modules that we need for our future use.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

dataset = load_boston()
dataset

dfx = pd.DataFrame(dataset.data, columns=dataset.feature_names) #original boston dataset
dfy = pd.DataFrame(dataset.target, columns=["MEDV"]) #load target attribute and make MEDV dataset
df = pd.concat([dfx, dfy], axis=1) #combine original boston dataset and MEDV dataset
df = pd.DataFrame(df)
df.MEDV.describe()

df.describe().round(2)

"""Once we have data we can do some exploratory analysis"""

cor_data = df.corr().round(2)

df.plot(kind='scatter',
        x = 'RM',
        y = 'MEDV',
        color = 'red',
        figsize = (5,4)

)

X = df['RM'].round(2)
X

y = df['MEDV'].round(2)

"""Do some visualization

"""

plt.style.use('classic')
plt.scatter(X,y)
plt.title('Rooms vs Median Price Per SQFT')
plt.xlabel('Rooms')
plt.ylabel('Per SQFT')
plt.show()

"""Model fitting (Univariate Version of Linear Regression)"""

# Making data preprossing
X_train , X_test , y_train , y_test = train_test_split(X,y,test_size=0.2 , random_state=1)

X_train = X_train.reshape(-1, 1)
y_train = y_train.values.reshape(-1, 1)
X_test = X_test.values.reshape(-1, 1)
y_test = y_test.values.reshape(-1, 1)

model = LinearRegression()

model.fit(X_train , y_train)

y_predicted = model.predict(X_test)

y_predicted.shape

# Model visualizastion
plt.title('Room VS Price/sqft')
plt.scatter(X_train , y_train , label='Training Data' , color='orange')
plt.scatter(X_test , y_test , label='Testing Data' , color='red')
plt.plot(X_test , y_predicted , label='Predicted Data' , color='blue')
plt.xlabel('RM')
plt.ylabel('Price / sqft')
plt.legend(loc='upper left')
plt.show()

input_value = 67

y_mainmodel = model.predict([[input_value]])
print('House Price for the main model predicted as $' + str(y_mainmodel[0][0]) +  ' per/sqft')

model.intercept_

model.coef_

"""Testing manually using y = mx + b. where b is significant as intercept and m is representing the slope. At a same time, x is the input"""

y_test_manual_predict = 8.76178391*input_value + (-32.40478223)
print('House Price for the manual model predicted as $' + str(y_test_manual_predict) +  ' per/sqft')
