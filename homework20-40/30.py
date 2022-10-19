list1=[35,46,57,13,24,35,99,68,13,79,88,46]
list2=[]
for x in list1:
    if x not in list2:
        list2.append(x)
list2.sort()
list3=list2[::-1]
print (list3)