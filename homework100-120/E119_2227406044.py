f=open('word.txt','r')
lst=f.readlines()
f.close()
with open('new_word.txt','w') as t:
    for i in lst:
        i=i.strip()
        lst1=i.split(' ')
        for j in lst1:
            if j[0]!='a' and j[0]!='e' and j[0]!='i' and j[0]!='o' and j[0]!='u':
                t.write(j)
                t.write('\n')