# -*- UTF-8 -*-
"""
题目：计算 s=a+aa+aaa+aaaa+aa...a 的结果，其中 a 是 0-9 的数字，有 n 个数相加（最大的数有
n 位）。例如 2+22+222+2222+22222(此时共有 5 个数相加)。编写程序，随机生成 a，从
键盘输入n，将公式进行输出，并输出计算结果。
"""

import random

def assignment61(a,n):
    '''
    param a: 是 0-9 的数字
          n: 最大数的位数
    reval: result=a+aa+aaa+aaaa+aa...a 
    例子： a :1 n:2
    result=1+11=12
    '''
    lst=[]
    res=0
    al=0
    for i in range (0,n):
        res+=a*(10**i)
        lst.append(res)
    for i in lst:
        al+=i
    return al
    pass  # 占位语句，完成函数后删除


if __name__ == '__main__':
    #初始化a是一个0-9的数字
    a=random.randrange(10)
    #输入n
    n=random.randrange(10)
    print("a={0:2d}; n={1:3d}".format(a,n))
    result=assignment61(a,n)
    print(result)