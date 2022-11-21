# -*- UTF-8 -*-
"""
51题：从键盘输入一个十进制正整数，利用列表和除二取余法，计算出该数字的二进制值。。
"""

def assignment51(num):    
    '''
    function: 计算整数的二进制数字序列
    :param:  num---十进制正整数 
    :return: 二进制数值构成的列表
    
    例子：
    num=10
    result=[1,0,1,0] #0b1010    
    num=5
    result=[1,0,1] #0b101
    '''
    lst1=[]
    while num > 0:
        a=num%2
        num//=2
        lst1.append(a)
    lst2=lst1[3::-1]
    return lst2
   

import random
if __name__ == '__main__':
    #输入一个十进制数num
    num= 5
    result=assignment51(num)
    print(num,":", result)
