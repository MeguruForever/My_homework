f=open('Numbers.txt','r')
numberlst=f.readlines()
f.close()
with open('Sort.txt','w') as t:
    lst=[]
    for i in numberlst:
        fl=float(i)
        lst.append(fl)
        lst=sorted(lst)
    count=0
    for j in lst:
        t.write(str(j))
        t.write('\n')
        count+=j*2
    average=sum(lst)/len(lst)
    variance=count/len(lst)
    t.write(str(average))
    t.write('\n')
    t.write(str(variance))
