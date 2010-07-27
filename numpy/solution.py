## 
## Author: John Stachurski
## Filename: solution.py
## Solution to Problems 1--3
##

import pylab

infile = open("table2.csv", 'r')
lines = infile.readlines()
infile.close()

del lines[0]     # Remove the first line
lines.reverse()  # Reverse order to start at earliest date

dates = []
values = []
for line in lines:
    elements = line.split(',')
    dates.append(elements[0])
    values.append(float(elements[-1]))

def seriesplot():
    "Plots the whole time series."
    pylab.plot(values)
    pylab.show()

def returnsplot(start_year, end_year):
    "Plots daily returns from start_year to end_year."
    plotvals = []
    for value, date in zip(values, dates):
        year = int(date.split('-')[0])  # extract the year
        if start_year <= year <= end_year:
            plotvals.append(value)
    pylab.plot(percent_change(plotvals))
    pylab.show()

def densityplot():
    """Plots a histogram of daily returns, as well as a
    fitted normal density."""
    dailyreturns = percent_change(values)
    pylab.hist(dailyreturns, bins=200, normed=True)
    m, M = min(dailyreturns), max(dailyreturns)
    mu = pylab.mean(dailyreturns)
    sigma = pylab.std(dailyreturns)
    grid = pylab.linspace(m, M, 100)
    densityvalues = pylab.normpdf(grid, mu, sigma)
    pylab.plot(grid, densityvalues, 'r-')
    pylab.show()
    
def percent_change(data):
    """Calculates change in percentages.
    Parameters: data is an array of floats.
    Returns: an array of length len(data) - 1.
    """
    X =[]
    for next, current in zip(data[1:], data[:-1]):
        X.append(100 * (next - current) / current)
    return X

if __name__ == '__main__':
	#densityplot()
	seriesplot()
	
