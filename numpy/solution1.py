## 
## Author: John Stachurski
## Filename: solution2.py
## Solution to Problem 4
##


from pylab import plot, show
from solution import dates, values   # Get data from the file solution.py

plotdata = []
# Append the first data entry for plotting
plotdata.append(values[0])
# Get the month corresponding to the first data entry
month = dates[0].split('-')[1]

for value, date in zip(values, dates):
    current_month = date.split('-')[1]
    if current_month == month:
        pass  # Do nothing
    else:
        plotdata.append(value)
        month = current_month

plot(plotdata)
show()
