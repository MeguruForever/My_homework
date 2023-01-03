f=open('students_data.txt','r')
lst=f.readlines()
f.close()
lst1=[]
for i in lst:
    i=i.strip()
    lst1.append(i)
choice=str(input('''a: 读取所有学生信息。 
b: 输出所有学生信息到屏幕上，要求每个学生信息占一行，学号占 10 列、左对齐，
姓名占 15 列、左对齐，年级占 5 列、右对齐。 
c: 对所有学生根据其学号按照从小到大排序。
d: 删除学号小于指定值 s1 的所有学生，其中 s1 由键盘输入。
请选择功能:'''))
if choice=='a':
    for i in lst1:
        print(i)
elif choice=='b':
    for j in lst1:
        lst2=j.split(' ')
        id='{:<10s}'.format(lst2[0])
        name='{:<15s}'.format(lst2[1])
        grade='{:5s}'.format(lst2[2])
        print(id,name,grade)
elif choice=='c':
    lst4=[]
    for j in lst1:
        lst3=j.split(' ')
        lst4.append(lst3)
        lst4=sorted(lst4,key=lambda x:x[0])
    for m in lst4:
        print(m)
elif choice=='d':
    number=int(input('请输入学号指定值：'))
    lst6=[]
    for k in lst1:
        lst5=k.split(' ')
        if int(lst5[0])>=number:
            print(lst5)




    
