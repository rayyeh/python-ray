from builtins import object
from ctypes import *
from ctypes.util import find_library

print '---Begin Show----'

print find_library('c')
print windll.kernel32
print cdll.msvcrt
print find_library('wapicd')
libc = cdll.LoadLibrary("msvcr90.dll")

print "---------- char --------"
x = c_char_p("Hello World")
print x
print x.value
print sizeof(x)

print '---------- int ----------'
i = c_int(42)
print i
print i.value

p = create_string_buffer("Hello", 10)
print sizeof(p), repr(p.raw)

print "---------- Bo class---------------"


class Bo(object):
    def __init__(self, number):
        self._as_parameter_ = number


bo = Bo(33)
printf = libc.printf
printf("%d bottles of beer \n", bo)

strchr = libc.strchr
print strchr('abcdef', ord('c'))
strchr.restype = c_char_p  # set retyrn type is char_pointer
print strchr('abcdef', ord('d'))

print '----Passing by reference byref()---------'
i = c_int()
f = c_float()
s = create_string_buffer('\000' * 32)
print i.value, f.value, repr(s.value)

libc.sscanf("1 3.14 hello", "%d %f %s", byref(i), byref(f), s)  # Passing by ref
print i.value, f.value, repr(s.value)

print '---- Pointer  pointer()---------'
ptr_i = pointer(i)  # use pointer()
ptr_f = pointer(f)
ptr_s = pointer(s)
libc.sscanf("1 3.14 hello", "%d %f %s", ptr_i, ptr_f, ptr_s)
print i.value, f.value, repr(s.value)
print 'point of i:', ptr_i.contents  # show contents
print 'point of f:', ptr_f.contents
print 'point of s:', ptr_s.contents

print  '------------ Test Structure ---------'


class POINT(Structure):  # Define Structure
    _fields_ = [('x', c_int), ('y', c_int)]


p = POINT(10, 20)
print p.x, p.y


def testptr(a):  # return type is POINT()
    b = POINT()
    b = a
    b.x = a.x + 100
    b.y = a.y + 100
    return b


t = testptr(p)
print 'value of t is :', t, ' Type of t is', type(t)

testptr.restype = POINT()  # POINT()
g = testptr(p)
print g.x, g.y

     



