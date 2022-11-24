#  编写一个函数，计算一个整数的所有因子之和，其中因子不包括整数本身，并编写测试
# 程序，在测试程序中输入整数和输出整数的所有因子之和。例如：输入 8，调用该函数
# 之后，得到结果为 7。

def assignment88(n):
    '''
    fucntion：计算一个整数的所有因子之和，因子不包括本身
    para：n---输入的整数
    return:res---所有因子之和
    example:
        8===>7
        16===>15
    '''
    lst=[]
    for i in range(1,n):
        if n%i==0:
            lst.append(i)
    res=0
    for i in lst:
        res+=i
    return res

    pass   #占位语句，添加代码后删除pass
    


if __name__ == '__main__':
    #输入一个整数
    n = 9

    result = assignment88(n)
    print(result)