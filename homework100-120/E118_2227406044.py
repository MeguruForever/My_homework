f=open('config.txt','r')
lst=f.readlines()
f.close()
with open('new_config.txt','w') as t:
    for i in lst:
        i=i.strip()
        lst1=i.split(':')
        m='<{:s}>{:s}</{:s}>'.format(lst1[0],lst1[1],lst1[0])
        t.write(m)
        t.write('\n') 