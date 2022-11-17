# # The CSV File Fotmat
# # One simple way to store data in a text file is to write the data as a series of values separated by commas, which is called comma-separated values.

# # Parsing the CSV File Headers
# # Pythons csv module in the standard library parses the lines in a CSV file and allows us to quickly extract the values

# import csv

# filename = 'data/sitka_weather_07-2018_simple.csv'
# with open(filename) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#     print(header_row)
    
#     # Output in terminal
#     # ['STATION', 'NAME', 'DATE', 'PRCP', 'TAVG', 'TMAX', 'TMIN']
    
#     for index, column_header in enumerate(header_row):
#         print(index, column_header)
        
#         # The enumerate() function returns both the index of each item and the value of each item as you loop through a list.

# # Output in terminal
# #  ['STATION', 'NAME', 'DATE', 'PRCP', 'TAVG', 'TMAX', 'TMIN']
# #     0 STATION
# #     1 NAME
# #     2 DATE
# #     3 PRCP
# #     4 TAVG
# #     5 TMAX
# #     6 TMIN

# # Extracting and Reading Data
# # Now that we know which columns of data we need, lets read in some of that data. Furst we'll read in the high temperature of each day.

# import csv

# filename = 'data/sitka_weather_07-2018_simple.csv'
# with open(filename) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
    
#     # Get high temperatures from this file.
#     highs = []
#     for row in reader:
#         high = int(row[5])
#         highs.append(high)

# print(highs)

# # Made an empty list called highs and then loop through the remaning rows in the file.
# # The reader object continues from where it left off in the csv file and automatically returns each line following its current position.
# # Then we pull the data from index 5 which is TMAX, we use int to convert the data which is stored as a string to numerical format.
# # We then append values to highs


# # Plotting Data in a Temperature Chart

# import csv

# import matplotlib.pyplot as plt

# filename = 'data/sitka_weather_07-2018_simple.csv'
# with open(filename) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
    
#     # Get high temperatures from this file.
#     highs = []
#     for row in reader:
#         high = int(row[5])
#         highs.append(high)
        
#     # Plot the high temperatures
#     plt.style.use('seaborn')
#     fix, ax = plt.subplots()
#     ax.plot(highs, c='red')
    
#     # Format Plot
#     ax.set_title("Daily high temperatures, July 2018", fontsize=24)
#     ax.set_xlabel('', fontsize = 16)
#     ax.set_ylabel("Temperature (F)", fontsize=16)
#     ax.tick_params(axis='both', which='major', labelsize=16)
    
# plt.show()


# # The datetime Module

# # Lets add dates to our graph to make it more useful. The first date from the weather data file is in the second row of the file.


# import csv
# from datetime import datetime

# import matplotlib.pyplot as plt

# filename = 'data/sitka_weather_07-2018_simple.csv'
# with open(filename) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
    
#     # Get dates and high temperatures from this file.
#     dates, highs = [], []
#     for row in reader:
#         current_date = datetime.strptime(row[2], '%Y-%m-%d')
#         high = int(row[5])
#         dates.append(current_date)
#         highs.append(high)
        
#     # Plot the high temperatures
#     plt.style.use('seaborn')
#     fix, ax = plt.subplots()
#     ax.plot(dates, highs, c='red')
    
#     # Format Plot
#     ax.set_title("Daily high temperatures, July 2018", fontsize=24)
#     ax.set_xlabel('', fontsize = 16)
#     fig.autofmt_xdate()
#     ax.set_ylabel("Temperature (F)", fontsize=16)
#     ax.tick_params(axis='both', which='major', labelsize=16)
    
# plt.show()

# We create two empty lists to store the dates and high temperatures from the file.
# We then convery the data containing the date information to datetime object and append it to dates.
# The call to fig.autofmt_xdate() draws the date labels diagonally to prevent them from overlapping.


# Plotting a Longer Timeframe


import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_07-2018_simple.csv'
filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # Get dates and high temperatures from this file.
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        dates.append(current_date)
        highs.append(high)
        
    # Plot the high temperatures
    plt.style.use('seaborn')
    fix, ax = plt.subplots()
    ax.plot(dates, highs, c='red')
    
    # Format Plot
    ax.set_title("Daily high temperatures -2018", fontsize=24)
    ax.set_xlabel('', fontsize = 16)
    # fig.autofmt_xdate()
    ax.set_ylabel("Temperature (F)", fontsize=16)
    ax.tick_params(axis='both', which='major', labelsize=16)
    
plt.show()



# Plotting a Second Data Series

# We can make our informative graph even more useful by including the low temperatures.
# We need to extract the low temperatures from the data file and then add them to our graph

import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_07-2018_simple.csv'
filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # Get dates and high temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
        
    # Plot the high temperatures
    plt.style.use('seaborn')
    fix, ax = plt.subplots()
    ax.plot(dates, highs, c='red')
    ax.plot(dates, lows, c='blue')
    
    # Format Plot
    ax.set_title("Daily high and low temperatures -2018", fontsize=24)
    ax.set_xlabel('', fontsize = 16)
    # fig.autofmt_xdate()
    ax.set_ylabel("Temperature (F)", fontsize=16)
    ax.tick_params(axis='both', which='major', labelsize=16)
    
plt.show()


# Shading an Area in the Chart

# Having added two data series, we can now examine the range of temperatures of each day. 
# Shading to show the range between each day's high & low temperatures.
# To do so use the fill_between() method, which takes a series of x values and two series of y values

import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_07-2018_simple.csv'
filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # Get dates and high temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
        
    # Plot the high temperatures
    plt.style.use('seaborn')
    fix, ax = plt.subplots()
    ax.plot(dates, highs, c='red', alpha=0.5)
    ax.plot(dates, lows, c='blue', alpha=0.5)
    ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
    
    # Format Plot
    ax.set_title("Daily high and low temperatures -2018", fontsize=24)
    ax.set_xlabel('', fontsize = 16)
    # fig.autofmt_xdate()
    ax.set_ylabel("Temperature (F)", fontsize=16)
    ax.tick_params(axis='both', which='major', labelsize=16)
    
plt.show()

# The alpha argument at controls a color's transparency. An alpha value of 0 is completely transparent, and 1 is opaque
# Setting 0.5 we make the red and blue plot lines appear lighter.
# The fill_between() the list of dates for the x values and then the two y values highs and lows.
# The facecolor argument determines the color of shaded region we git it a low alpha value of 0.1 so the fill region connects

