# load pandas
import pandas as pd

# read data as pandas dataframe
data = 'bigdata.csv'
df = pd.read_csv(data)

# print first three rows of the pandas dataframe
print(df.head(3))

# statistically describe the humidity data
print(df['Humidity'].describe())

# temp_is_too_low is a boolean variable (humidity too low)
humid_is_too_low = df['Humidity'] < 78.4
print(humid_is_too_low.head())

# filter rows for humidity < 78.4
less_than_784 = df[humid_is_too_low]
print(less_than_784.shape)

# print the first 4 rows for humidity < 78.4
print(less_than_784.head(4))

# humid_is_too_high is a boolean variable (humidity too high)
humid_is_too_high = df['Humidity'] > 93.7
print(humid_is_too_high.head())

# filter rows for humidity > 93.7
greater_than_937 = df[humid_is_too_high]
print(greater_than_937.shape)

# print the first 4 rows for humidity > 93.7
print(greater_than_937.head(4))



































































