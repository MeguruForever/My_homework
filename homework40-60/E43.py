# -*- UTF-8 -*-
'''
第43题：算数练习题。 编写一个程序， 实现 100 以内的随机四则运算出题， 将题目输出在屏幕上，
例如： 1+1=。然后接收用户输入，判断回答是否正确，将结果输出到屏幕上。如果回答
正确，则提示回答正确，如果错误在提示回答错误的同时，将正确答案输出。
'''
import random

#step1: 构建运算符列表
operatorLst=['+','-','*','/']

#step2: 产生两个100以内的整数
a=random.randrange(0,101)
b=random.randrange(0,101)
#step3: 产生一个[0,4)之间的整数index
index=random.randrange(0,4)
#step4: 根据index为下标选择operatorLst中的运算操作，并输出算式。如1+1=
answer=int(input("{0:d}{1}{2:d}=".format(a,operatorLst[index],b)))
#step5: 获取用户从键盘输入的结果

#step6: 判断用户输入的结果是否正确，并按题目要求给出判断结果。
if index==0:
    if a+b==answer:
        print ("yes")
    else:
        print ("no")
elif index==1:
    if a-b==answer:
        print ("yes")
    else:
        print ("no")
elif index==2:
    if a*b==answer:
        print ("yes")
    else:
        print ("no") 
elif index==3:
    if a/b==answer:
        print ("yes")
    else:
        print ("no")               