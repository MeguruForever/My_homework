f=open('students_data.txt','r')
lst=f.readlines()
f.close()
with open('students_5.txt','w') as t:
    for i in lst:
        i=i.strip()
        lst1=i.split(' ')
        if int(lst1[2])>3:
            t.write(lst1[0])
            t.write(' ')
            t.write(lst1[1])
            t.write('\n')
