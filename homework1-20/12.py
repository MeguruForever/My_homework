import math
x1,y1=eval(input("输入a点坐标用，隔开"))
x2,y2=eval(input("输入b点坐标用，隔开"))
x=(x1-x2)**2+(y1-y2)**2#距离的平方
l=math.sqrt(x)
print (l)