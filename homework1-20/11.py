import math
r,h=eval(input("输入整数水桶深和半径用，隔开"))
V=h*r**2*math.pi#筒子的体积
num=(20000//V)+1#多一同子水
print (format(num,'.0f'))