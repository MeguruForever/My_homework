import math
x1,y1=eval(input("输入a点坐标用，隔开"))
x2,y2=eval(input("输入b点坐标用，隔开"))
x3,y3=eval(input("输入c点坐标用，隔开"))
s1=(x1-x2)**2+(y1-y2)**2#三遍边长度
side1=math.sqrt(s1)
s2=(x2-x3)**2+(y2-y3)**2
side2=math.sqrt(s2)
s3=(x1-x3)**2+(y1-y3)**2
side3=math.sqrt(s3)
s=(side1+side2+side3)/2
area=math.sqrt(s*(s-side1)*(s-side2)*(s-side3))#面积公式
print (format(area,'7.2f'))

