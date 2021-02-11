import keras  # ML Library
import matplotlib.pyplot as plt  # Used to graph our results
import pandas as pd  # Data Handling Library

df=pd.read_csv('prices.csv')


squareFeet = df[['SquareFeet']].values #x value
salePrice = df[['SalePrice']].values #y value

model = keras.Sequential()
model.add(keras.layers.Dense(1, input_shape=(1,)))
model.compile(keras.optimizers.Adam(lr=1), 'mean_squared_error')

model.fit(squareFeet,salePrice, epochs=30, batch_size=10)

#Plot datapoints
df.plot(kind='scatter',
       x='SquareFeet',
       y='SalePrice', title='Housing Prices and Square Footage of Iowa Homes')


y_pred = model.predict(squareFeet) #The predicted housing price based on square feet

#Plot the linear regression line
plt.plot(squareFeet, y_pred, color='red')

newSF = 2000
print(model.predict([newSF]))