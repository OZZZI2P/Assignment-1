# load pandas
import pandas as pd

# read data as pandas dataframe
data = 'bigdata.csv'
df = pd.read_csv(data)

# print first three rows of the pandas dataframe
print(df.head(3))

# statistically describe the temperature data
print(df['Temperature'].describe())

# temp_is_too_low is a boolean variable (temperature too low)
temp_is_too_low = df['Temperature'] < 62.2
print(temp_is_too_low.head())

# filter rows for temperature < 62.2
less_than_622 = df[temp_is_too_low]
print(less_than_622.shape)

# print the first 4 rows for temperature < 62.2
print(less_than_622.head(4))

# temp_is_too_high is a boolean variable (temperature too high)
temp_is_too_high = df['Temperature'] > 79.6
print(temp_is_too_high.head())

# filter rows for temperature > 79.6
greater_than_796 = df[temp_is_too_high]
print(greater_than_796.shape)

# print the first 4 rows for temperature > 79.6
print(greater_than_796.head(4))

