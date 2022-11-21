# -*- UTF-8 -*-
'''
46题：小明带着 N 元钱去买酱油。酱油 15 块钱一瓶，商家进行促销，每买 3 瓶送 1 瓶，
或者每买 5 瓶送 2 瓶。请问小明最多可以得到多少瓶酱油。N 的数值 由用户输入，
并且一定是整数。
'''

def assignment46(money):
    '''
    功能：根据money计算最多能买的酱油数量
    参数: money---钱数
    返回值：最多能购买的酱油数量
    '''
    al=0
    num=money//15
    while num>=5:
        al+=7
        num-=5
    while num<5 and num >=3:
        al+=4
        num-=3
    al+=num
    return al
   #占位语句，添加代码后删除pass

    

if __name__ == '__main__':
    #step1: 输入钱数
    money =int( input("输入钱数"))
    #step2: 计算能购买的酱油数量
    result = assignment46(money)
    print("{0:d}元钱最多能购买{1:d}瓶酱油".format(money,result))