class Point(object):
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
        
    def __str__(self):
        return "("+str(self.x)+ "," +str(self.y) + ")"
    
p1=Point(1,2)
print p1
