# 编写程序，计算并输出由 0~7 所能组成的奇数的个数。

import math

def assignment86(digitalLst):
    '''
    fucntion：计算并输出由 0~7 所能组成的奇数的个数,每个数都必须出现一次并仅能出现一次，正确：10234567，不正确：01234567，11234567
    para: digitalLst---数字列表
    return:res
    '''
    res=0
    for i in range(1,8):
        if i%2==0:
            res+=math.factorial(7)*4/7
        if i%2!=0:
            res+=math.factorial(7)*3/7
    
    return res
    pass   #占位语句，添加代码后删除pass
    
if __name__ == '__main__':
    digitalLst = list(range(8))
    result = assignment86(digitalLst)
    print(result)
  
