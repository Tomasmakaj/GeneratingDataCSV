# The CSV File Fotmat
# One simple way to store data in a text file is to write the data as a series of values separated by commas, which is called comma-separated values.

# Parsing the CSV File Headers
# Pythons csv module in the standard library parses the lines in a CSV file and allows us to quickly extract the values

import csv

filename = 'data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
    
    # Output in terminal
    # ['STATION', 'NAME', 'DATE', 'PRCP', 'TAVG', 'TMAX', 'TMIN']
    
    for index, column_header in enumerate(header_row):
        print(index, column_header)
        
        # The enumerate() function returns both the index of each item and the value of each item as you loop through a list.

# Output in terminal
#  ['STATION', 'NAME', 'DATE', 'PRCP', 'TAVG', 'TMAX', 'TMIN']
#     0 STATION
#     1 NAME
#     2 DATE
#     3 PRCP
#     4 TAVG
#     5 TMAX
#     6 TMIN

# Extracting and Reading Data
# Now that we know which columns of data we need, lets read in some of that data. Furst we'll read in the high temperature of each day.

import csv

filename = 'data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # Get high temperatures from this file.
    highs = []
    for row in reader:
        high = int(row[5])
        highs.append(high)

print(highs)

# Made an empty list called highs and then loop through the remaning rows in the file.
# The reader object continues from where it left off in the csv file and automatically returns each line following its current position.
# Then we pull the data from index 5 which is TMAX, we use int to convert the data which is stored as a string to numerical format.
# We then append values to highs


# Plotting Data in a Temperature Chart

import csv

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # Get high temperatures from this file.
    highs = []
    for row in reader:
        high = int(row[5])
        highs.append(high)
        
    # Plot the high temperatures
    plt.style.use('seaborn')
    fix, ax = plt.subplots()
    ax.plot(highs, c='red')
    
    # Format Plot
    ax.set_title("Daily high temperatures, July 2018", fontsize=24)
    ax.set_xlabel('', fontsize = 16)
    ax.set_ylabel("Temperature (F)", fontsize=16)
    ax.tick_params(axis='both', which='major', labelsize=16)
    
plt.show()


# The datetime Module

# Lets add dates to our graph to make it more useful. The first date from the weather data file is in the second row of the file.


import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_07-2018_simple.csv'
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
    ax.set_title("Daily high temperatures, July 2018", fontsize=24)
    ax.set_xlabel('', fontsize = 16)
    fig.autofmt_xdate()
    ax.set_ylabel("Temperature (F)", fontsize=16)
    ax.tick_params(axis='both', which='major', labelsize=16)
    
plt.show()

# We create two empty lists to store the dates and high temperatures from the file.
# We then convery the data containing the date information to datetime object and append it to dates.
# The call to fig.autofmt_xdate() draws the date labels diagonally to prevent them from overlapping.