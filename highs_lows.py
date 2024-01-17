import csv
from matplotlib import pyplot as plt
from datetime import datetime

#get dates and high temperatures from the file

filename = "sitka_weather_2014.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
    
    dates, highs = [],[]
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)
        
        highs.append(row[1])
    print(highs)
    
#plot this data

fig = plt.figure (dpi = 128, figsize =(10,10))
plt.plot(dates, highs, c = 'red')

#format the plot

plt.title("Daily Temperatures, - 2014", fontsize = 24)
plt.xlabel('', fontsize = 16) 
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()