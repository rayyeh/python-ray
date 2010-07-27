import pylab
import random
n=500
data =[random.normalvariate(0,1) for i in range(n)]
pylab.hist(data,bins=40)
pylab.show()
