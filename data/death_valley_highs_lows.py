import csv

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    for index, column_header in enumerate(header_row):
        print(index, column_header)
        
        
        
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
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
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
    title = "Daily high and low temperatures -2018\nDeathV Valley, CA"
    ax.set_title(title, fontsize=20)
    ax.set_xlabel('', fontsize = 16)
    # fig.autofmt_xdate()
    ax.set_ylabel("Temperature (F)", fontsize=16)
    ax.tick_params(axis='both', which='major', labelsize=16)
    
plt.show()


# (studysession) (base) tomasmakaj@Tomass-MBP StudySession % /Users/tomasmakaj/Desktop/StudySession/StudySession/bin/python /Users/tomasmakaj/Desktop/StudySession/deat
# h_valley_highs_lows.py
# Traceback (most recent call last):
#   File "/Users/tomasmakaj/Desktop/StudySession/death_valley_highs_lows.py", line 16, in <module>
#     high = int(row[4])
#            ^^^^^^^^^^^
# ValueError: invalid literal for int() with base 10: ''
# (studysession) (base) tomasmakaj@Tomass-MBP StudySession % 

# This error tells us that Python can't process the high temperature for one of the dates because it cant turn an empty string('') into int
# Lets run error-checking code when the vales are being read from the CSV file to handle exceptions that might arise

# Each time we examine a row we try to extract the date and the high and low temperature.
# If any data is missing Python willl raise a ValueError and 
# We handle it by printing an error message that includes the date of the missing data
# Python will plot the data and also give back the missing data in the output terminal