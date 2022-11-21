# -*- UTF-8 -*-
"""
53题：随机生成一个数[0-100],判断这个数是否等于 50，如果不等于则重新随机生成。最后输
出一共随机生成了多少次
"""
import random
def assignment53():
    '''
    返回：[lst,res]:lst每次生成的随机数的存放列表,res表示共随机生成了多少次
    返结果示例：[[25,6,42,50],4]
    '''
    res=1
    a=random.randrange(0,101)
    while a !=0:
        a=random.randrange(0,101)
        res+=1
    return res


if __name__ == '__main__':
    result = assignment53()
    print(result)