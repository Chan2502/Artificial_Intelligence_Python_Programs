import pandas as pd
import numpy as np

url="C:\\Users\\Lenovo\\Downloads\\e.csv"
dp=pd.read_csv(url)
print(dp)
st=dp.shape
print(st)
print(type(dp))
print(dp.head(4))
print(dp.tail(4))
df=dp.replace('?',np.nan)
print(df)
# Missing values
ds=df.isnull().sum()
print(ds)
# Null Values
print(dp.info())

print(dp.describe())
# The Most expensive car
most_exp_car = dp[["company"]][dp.price == dp.price.max()]
print('most expensive car:- ')
print(most_exp_car)
# group all the toyota
car_Manufacturers = dp.groupby('company')
toyotaDf = car_Manufacturers.get_group('toyota')
print(toyotaDf)