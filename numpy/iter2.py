import pylab

         
def f(r,t):
    i=0
    while i < t:
        r = 4*(1-r) *r
        yield r
        i=i+1
    
h=f(0.1, 100)
 
time_series=[x for x in h]
pylab.plot(time_series)
pylab.show()
