import math
import numpy
import random
a=random.uniform(10,50)
b=random.uniform(10,50)
x=complex(a,b)
mo=math.sqrt(a**2+b**2)
arg1=a/mo
answer=math.acos(arg1)
print (answer*180/math.pi,"°")