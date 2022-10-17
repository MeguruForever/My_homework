import random
list1=[]
unm=random.randrange(1,20)
for i in range(unm):
    a=random.randrange(1,20)
    if a%2==0:
        list1.append(a)
    else:continue
if unm in list1:
    print ("存在")
else:print ("不存在")