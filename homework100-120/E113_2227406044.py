f=open('article.txt','r')
article=f.read()
article=article.strip()
f.close()
with open('new_article.txt','w') as t:
    lst=article.split('.')
    for i in lst:
        if i == '':
            continue
        else:
            i=i[0].upper()+i[1:]
            t.write(i)
            t.write('.\n')
        
       
