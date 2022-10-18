import random
a=random.randint(1,50)
list1=random.sample([i for i in range (100)],a)
print (list1)
list2=[]
for i in list1:
    if i==2:list2.append(i)
    for j in range(2,i):
        if i%j==0:
            break
        if j==i-1:
            list2.append(i)
        else:
            continue

print (list2)