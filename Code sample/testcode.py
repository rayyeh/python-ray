import sys

print 'test'
for a in range(0,10):
    for b in range(0,10):
        for c in range(0,10):
            for d in range(0,10):
                 #print a,b,c,d
                 if 10*a+b+10*c+a == d*10+a and 10*a+b-10*c-a ==a :
                        print a,b,c,d 
                        break
                        
y=1
for i in range(1,2001):
    if i == 1: 
        i=1
    if i > 1:
        y= y*i
x=str(y)
print len(x)
        
    