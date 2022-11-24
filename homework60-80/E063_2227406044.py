# -*- UTF-8 -*-
"""
题目：假设某人每月计划给地铁卡充一些钱用于坐公交， 已知当地地铁票费用按照下表进行计
算。 编写一个程序， 从键盘输入充值金额， 计算并输出充值的金额最多能坐多少次公交。
当月累计次数 票价
1~10 2 元（原价）
10~20 原价 9.5 折
21-50 原价 8 折
51 次以上 原价 5 折
"""

def assignment63(money, price=2):
    '''
    function: 根据公交票价，计算能乘坐的次数
    param:  money---充值的金额
            price---单次公交车票价(原价)
    reval: count:最多能坐多少次公交
    '''
    count=0
    while count<=10:
        money-=2
        count+=1
        if money<0:
            return count
    while count>10 and count <=20:
        money-=2*0.95
        count+=1
        if money<0:
            return count
    while count>20 and count <=50:
        money-=2*0.8
        count+=1
        if money<0:
            return count
    while count>50:
        money-=1
        count+=1
        if money<0:
            return count
    # 占位语句，完成函数后删除

if __name__ == '__main__':
    #step1: 键盘输一个money
    money=500
    print(assignment63(money))
    # result=assignment63(money,2)
    # print("最多能坐公交的次数",result)
