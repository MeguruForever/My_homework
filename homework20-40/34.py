"""
如3×3的魔方阵： 
    8   1   6 
    3   5   7 
    4   9   2  
魔方阵的排列规律如下：
(1)将1放在第一行中间一列；
(2)从2开始直到n×n止各数依次按下列规则存放；每一个数存放的行比前一个数的行数减1，列数加1（例如上面的三阶魔方阵，5在4的上一行后一列）；
(3)如果上一个数的行数为1，则下一个数的行数为n(指最下一行);例如1在第一行，则2应放在最下一行，列数同样加1；
(4)当上一个数的列数为n时，下一个数的列数应为1，行数减去1。例如2在第3行最后一列，则3应放在第二行第一列；
(5)如果按上面规则确定的位置上已有数，或上一个数是第一行第n列时，则把下一个数放在上一个数的下面。例如按上面的规定，4应该放在第1行第2列，但该位置已经被占据，所以4就放在3的下面；
"""
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

    
    

