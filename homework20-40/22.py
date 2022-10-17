import random
a=random.randint(1,100)
list1=random.sample([i for i in range (1000)],a)#生成随机数量的数组
list1.sort()
list2=list1
if a % 2 ==1:#单数时
    num1=(a//2)-1
    print (list2[num1])
else:#偶数时
    num2=(a//2)-1
    print (list2[num2])



    