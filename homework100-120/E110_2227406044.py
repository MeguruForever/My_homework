f=open('cat2.txt','r')
content=f.read()
f.close()
t=open('cat1.txt','a')
t.write('\n')
t.write(content)
t.close()