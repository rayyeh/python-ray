import random, os, Gnuplot

mean = 3
strdev =  10
ns = [10, 100, 1000, 10000]
g = Gnuplot.Gnuplot()
g('set multiplot')
g('set size 0.5,0.5')

for i in range(0, 4):
 gauss = list()
 for j in range(0, ns[i]):
     gauss.append(list())
     gauss[j].append(random.gauss(mean, strdev))
     gauss[j].append(random.gauss(mean, strdev))

 if i == 0:
     g('set origin 0,0.5')
 elif i == 1:
     g('set origin 0.5,0.5')
 elif i == 2:
     g('set origin 0,0')
 else:
     g('set origin 0.5,0')

 g.plot(gauss)

g('unset multiplot')
raw_input('Please press return to continue...\n') 
