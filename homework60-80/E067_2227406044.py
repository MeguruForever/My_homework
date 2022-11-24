# -*- UTF-8 -*-
"""
题目：提示用户输入一个整数 n,然后输出 [1,n) 之间所有的素数。提示：质数（prime number）
又称素数，有无限个。质数定义为在大于 1 的自然数中，除了 1 和它本身以外不再有其
他因数的数称为质数。 例：输入 n = 10。输出：2，3，5，7
"""


def assignment67(n):
    '''
    功能：输出[1,n)之间的所有素数
    参数：n输入的整数
    返回值：res:[1,n)之间的所有素数
    返回值示例：n=10 ==>[2,3,5,7]
    '''   #占位语句，添加代码后删除pass
    lst=[]
    for i in range(n):
        if i==0:
            continue
        if i==1:
            continue
        for j in range (2,i):
            if i%j==0:
                break
        else:
            lst.append(i)
    return lst


if __name__ == "__main__":
    # step1:提示用户输入n
    n= 15
    print(n)
    # step2:调用函数输出[1,n)之间的所有素数
    result = assignment67(n)
    print(result)
