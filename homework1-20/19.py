import math


f1=list(map(int,input("输入一个向量的两个数字0到1之间用逗号隔开").split(",")))
f2=list(map(int,input("再输入一个向量的两个数字0到1之间用逗号隔开").split(",")))
x1=f1[0]
y1=f1[1]
x2=f2[0]
y2=f2[1]
ji=x1*x2+y1*y2
a=math.sqrt(x1**2+y1**2)
b=math.sqrt(x2**2+y2**2)
cos1=ji/a/b
print (cos1)