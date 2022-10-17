import random
list1=[]
for i in range (10):
    a=random.randint(1,10)
    list1.append(a**2)
list1.sort()
list2=list1[::-1]
print (list2)