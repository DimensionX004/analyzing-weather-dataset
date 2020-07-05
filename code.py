# --------------
#Importing the modules
import pandas as pd
import numpy as np
from scipy.stats import mode 


#Code for categorical variable
def categorical(df):
    categorical = pd.Categorical(weather)
    return categorical


#Code for numerical variable
def numerical(df):
    numerical = df.select_dtypes([np.number]).columns
    return numerical


#code to check distribution of variable
def clear(df,col,val):
    clear_cloudy = df[df['Weather']== 'Cloudy']
    value_counts = clear_cloudy.count()
    return value_counts


#Code to check instances based on the condition
def instances_based_condition(df,col1,val1,col2,val2):
    instance = df[(df['Wind Spd (km/h)']>35) & (df['Visibility (km)']==25)]
    return instance



# Code to calculate different aggreagted values according to month

def agg_values_ina_month(df,date_col,agg_col, agg):
    aggregated_value = pd.pivot_table(df, index = date_col, values = agg_col, aggfunc = agg)
    return aggregated_value


# Code to group values based on the feature
def group_values(df,col1,agg1):
    grouping = df.groupby(col1).agg(agg1)
    return grouping


# function for conversion 
def convert(df,celsius):
    converted_temp = df[celsius].apply(lambda x: (1.8*x)+32)
    return converted_temp


# Load the weather_2012 data csv file and store it in weather variable. The path of the dataset has been stored in the variable `path` for you.
weather = pd.read_csv(path)
#print(weather.head(5))

# As you have now loaded the weather data you might want to check the categorical and numerical variables. You can check it by calling categorical and numerical function. 
cat = categorical(weather)
#print(cat)
num = numerical(weather)
#print(num)


#You might be interested in checking the distribution of a specific value like the number of times the weather was exactly Cloudy in the given column. Feel free to check on other values.
#You can check it by calling the function clear with respective parameters.
#By using index of the value or name of the value you can check the number of count
cl = clear(weather, 'Weather', 'Cloudy')
#print(cl)


# Now suppose you want to check some instances based on a specific condition like when the wind speed was above 35 and visibility was 25. You can dicretly check it by calling the function instances_based_condition with respective parameters.
wind_speed_35_vis_25 = instances_based_condition(weather, 'Wind Spd (km/h)', 35, 'Visibility (km)', 25)
#print(wind_speed_35_vis_25)


#You have temperature data and want to calculate the mean temperature recorded by month.You can generate a pivot table which contains the aggregated values(like mean, max ,min, sum, len) recoreded by month. 
#You can call the function agg_values_ina_month with respective parameters. 
weather['Month'] = weather['Date/Time'].str.slice(5,7).astype(int)
mean_by_month = agg_values_ina_month(weather, 'Month', 'Temp (C)', {'Temp (C)':[np.mean,max,min,sum, len]})
del weather['Month']
#print(mean_by_month.head(5))

# To groupby based on a column like you want to groupby on Weather column and then aggregate the mean values of each column for different types of weather using mean. You can call the function group_values.
# Feel free to try on diffrent aggregated functions like max, min, sum, len
mean_weather = group_values(weather, 'Weather', np.mean)
#print(mean_weather)

# You have a temperature data and wanted to convert celsius temperature into fahrehheit temperatures you can call the function convert.
conv = convert(weather, 'Temp (C)')
#print(conv)



