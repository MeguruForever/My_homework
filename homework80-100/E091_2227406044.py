#  编写一个递归函数，求解 Fibonacci 数列（兔子繁殖）问题的某项的值。编写测试程序，
# 从键盘输入指定项，并输出 Fibonacci 数列指定项的值。


def assignment91(n):
    '''
    fucntion：计算Fibonacci数列的指定项的值
    para：n---输入的整数
    return:Fibonacci值
    example:
        10===>55
        16===>987
    '''
    if n==1 or n==2:
        return 1
    return assignment91(n-1)+assignment91(n-2)

    pass   #占位语句，添加代码后删除pass
    


if __name__ == '__main__':
    #输入一个整数
    n = 9

    result = assignment91(n)
    print(result)