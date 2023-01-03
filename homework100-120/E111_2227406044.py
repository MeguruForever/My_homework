f=open('StrInts.txt','r')
number=f.read()
f.close()
lst=number.split( )
with open('ResultInts.txt','w') as t:
    count=0
    for i in range(len(lst)):
        if int(lst[i])>=0 and i%2==0 and int(lst[i])%2==1:
            string='{:8d}'.format(int(lst[i]))             
            t.write(string)           
            count+=1
        if count==3:
            t.write('\n')
            count=0
  