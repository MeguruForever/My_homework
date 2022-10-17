import random
a=random.randint(1,100)
list1=random.sample([i for i in range (1000)],a)#生成随机数量的数组
list2=list1[::-1]
if list1==list2:
    print ("是回文")
else:print ("不是回文")

