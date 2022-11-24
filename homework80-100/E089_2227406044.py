# 编写一个函数，将一个整数的各位数字对调，并编写测试程序，在测试函数中输入整数
# 和输出新的整数。例如：输入 123，调用该函数之后，得到结果为 321

def assignment89(n):
    '''
    fucntion：将整数对调
    para：n---输入的整数
    return:对调后的结果
    example:
        123===>321
        120 ===>21
    '''
    lst=list(str(n))
    lst1=lst[::-1]
    if lst1[0]=='0':
        lst1.remove('0')
    answer=''
    for i in lst1:
        answer+=i
    return int(answer)
        

    
    pass   #占位语句，添加代码后删除pass
    


if __name__ == '__main__':
    #输入一个整数
    n = 120

    result = assignment89(n)
    print(result)