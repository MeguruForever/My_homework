list1=[]
for x in range (501):
    if x==2:
        list1.append(x)
    for y in range (2,x):
        if x%y==0:
            break
        elif y==x-1:
            list1.append(x)
        else:continue
res=0
for x in list1:
    print(list1[res],list1[res+1],list1[res+2],list1[res+3],list1[res+4]) 
    
    if list1[res+4]==499:
        break
    res+=5