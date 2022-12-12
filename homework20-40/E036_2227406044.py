#36题：随机生成一个[0~100]的整数，判断这个数是奇数还是偶数。

import random

def assignment36(num):
    if num%2==0:
        return True
    else:
        return False
    '''
    功能：判断整数num的奇偶性
    返回值：True---偶数，False---奇数
    '''
    
   #占位语句，添加代码后删除pass

    
if __name__ == '__main__':
    #step1: 产生[0~100]随机整数
    num = random.randrange(0,100)

    #step2: 调用函数判断num的奇偶性 
    result = assignment36(num)
    if result == True:
        print("整数{0:4d}是偶数".format(num))
    else:
        print("整数{0:4d}是奇数".format(num))