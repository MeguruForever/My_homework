import random

n=int(input("输入一个奇数n")) 
al=n*n
list1=[0 for i in range(al)]#将矩阵平放成一条线
row1=0
locumn1=n//2
location=(row1*n)+locumn1
list1[location]=1#把一先放好

#安放后面的数
for x in range (2,al+1):
    if row1==0:#是否在最上一行
        row1=n-1#回到最后一行
    else :row1-=1#上一行
    if locumn1==n-1:#是否在最后一列
        locumn1=0#回到第一列
    else : locumn1+=1#下一列
    location1=(row1*n)+locumn1#定位
    if list1[location1]!=0:#定位区有东西了
        a=list1.index(x-1)#定位上一个数的位置
        location2=a+n#去上个数的下面
        list1[location2]=x#把当前数放进去
        b=list1.index(x)#定位当前数的位置
        row1=b//n#坐标行参数变成当前数的实际位置
        locumn1=b%n#坐标列参数变成当前数的实际位置
    else:list1[location1]=x     #正常放数
for o in range(n):
    print (list1[n*o:n+n*o:1])

    
    

