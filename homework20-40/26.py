list1=[1,3,4,6,6,7,8,8,10,21,22,22]
list2=[]
for a in list1:
    if a not in list2 and a < 10:
        list2.append(a)
print (list2)

        
