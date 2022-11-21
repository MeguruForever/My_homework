# -*- UTF-8 -*-
"""
52题：从键盘输入一个十六进制正整数，计算出该数字的二进制值。
"""

def assignment52(num):
    '''
    function: 
    param: num---一个十六进制整数
    return: 二进制数值组成的列表 
    例子：
    num=0Xa
    result=[1,0,1,0]#0b1010
    
    num=0X5
    result=[1,0,1] #0b101
    '''
    a=bin(num)
    lst1=[]
    lst=list(str(a))
    lst.remove('b')
    lst.remove('0')
    for i in lst:
        lst1.append(int(i))
        
    return lst1
    


if __name__ == '__main__':
    #输入一个十六进制数num; int(str,16)表示将字符串按照16进制方式转换成十进制整数
    num = int(input("请输入一个十六进制整数:"),16)
    result = assignment52(num)
    print(result)