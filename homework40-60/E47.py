# -*- UTF-8 -*-
'''
第47题：
假设银行对 1 年期的存款利息计算法方法如下：如果存款金额 I 小于 10 万元，则按照
1.5%的年利率计算利息；如果存款金额 I 大于等于 10 万元，但小于 50 万元，则按照
2%的年利率计算利息；如果存款金额 I 大于等于 50 万元，但小于 100 万元，则按照 3%
的年利率计算利息；如果存款金额大于等于 100 万元，则按照 3.5%的年利率计算利息。
现在从键盘输入一个整数表示存款金额，请计算一年后的本金和利息总共有多少，将计
算结果输出到屏幕上。
'''

def assignment47(money):
    '''
    功能：计算一年期存款与利息
    参数：money---存款数量
    返回值：本金+利息的和
    返回值示例：9*0.015+9=9.135
    '''
    if money<10:
        money+=money*0.015
    elif money>=10 and money<50:
        money+=money*0.02
    elif money>=50 and money<100:
        money+=money*0.03
    else:
        money+=money*0.035
    return money
       #占位语句，添加代码后删除pass
    

if __name__ == '__main__':
    #step1: 输入存款金额
    money = int(input("输入存款金额 是个整数"))
    #step2: 调用函数计算存款与利息
    result = assignment47(money)
    print("{0:.4f}万元一年的利息和本金有:{1:.4f}".format(money,result))