# -*- UTF-8 -*-
'''
第45题：制作一个选择菜单，用户从键盘输入选择。如果输入内容为 1、 2、 3 中的一个，输出选
择的语言名称+“是一款非常优秀的编程语言”；如果输入 4，则输出“退出成果”；输
入其他选项提示“选择有误”。菜单内容如下：
请选择你最喜欢的编程语言
[1]Python
[2]C++
[3]Java
[4]退出
'''

#step1: 获取用户输入
Choose=int(input("请选择你最喜欢的编程语言\n[1]Python\n[2]C++\n[3]Java\n[4]退出\n"))
#step2: 根据用户输入，输出相应的提示信息
if Choose==1:
    print("Python是一款非常优秀的编程语言")
elif Choose==2:
    print ("C++是一款非常优秀的编程语言")
elif Choose==3:
    print ("Java是一款非常优秀的编程语言")
elif Choose==4:
    print ("退出")
else:
    print ("选择有误")