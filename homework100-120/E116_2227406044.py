with open('Folder\\file1.txt','r') as f:
    content1=f.read()
with open('Folder\\file2.txt','r') as i:
    content2=i.read()
with open('Folder\\file3.txt','r') as j:
    content3=j.read()
with open('Folder\\file4.txt','r') as k:
    content4=k.read()
with open('Folder\\merge.txt','w') as l:
    l.write(content1)
    l.write('\n')
    l.write(content2)
    l.write('\n')
    l.write(content3)
    l.write('\n')
    l.write(content4)
    