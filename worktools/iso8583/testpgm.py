__author__ = 'rayyeh'
TotalSEND = 10
transet =['A','B','C']
PANLIST = {0:'a',1:'b',2:'c',3:'d',4:'e',5:'f'}
for req in range(TotalSEND):
    for t in transet:
        if req == 0:
            x = 0+transet.index(t)
        else:
            x = (req % len(PANLIST)+transet.index(t))
        print '============================'
        print 'Req %d,transet index:%d,PAN no:%d ' %(req,transet.index(t),x)

