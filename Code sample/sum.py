#summation.py
#use the * operator to indicate, that the function will accept arbitrary number of arguments
def sum(*args):
   ''' Test many args and return'''

   r=0
   for i in args:
      r +=i
   return r

print sum.__doc__
print sum(1,2,3)
print sum(1,2,3,4,5)


#person.py
#use the ** construct in our functions. In such a case, the function will accept a dictionary
def display(**details):
   for i in details:
      print "%s:%s" %(i,details[i])

display(name ='ray',age=43,sex='M',addr='adfad')

