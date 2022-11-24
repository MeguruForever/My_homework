# 通过[0,500]范围内随机数发生的方法分别创建两个整数数据的集合，要求每个集合中数
# 据的个数分别要超过 200 个。在此基础上实现：
# a) 求出两个集合中不相同的数据，并进行显示。要求每行显示 10 条，每个数占 5 列，
# 右对齐；
# b) 求出两个集合中相同的数据，并进行显示。要求每行显示 10 条，每个数占 5 列，
# 右对齐；

#step1:生成两个范围在0-500的个数不超过200的整数集合
import random
n=random.randrange(1,201)
lst1=[]
lst2=[]
for i in range(0,n):
    a=random.randrange(0,501)
    lst1.append(a)
for i in range(0,n):
    a=random.randrange(0,501)
    lst2.append(a)
lst1=tuple(lst1)
lst2=tuple(lst2)
#step2:求两个集合中不同的数据，按照要求打印
lst3=[]
for i in lst1:
    if i not in lst2:
        lst3.append(i)
print(tuple(lst3))
#step3:求两个集合中相同的数据，按照要求打印
lst4=[]
for i in lst1:
    if i in lst2:
        lst4.append(i)
print(tuple(lst4))
