# 反素数指一个素数将其逆向拼写后也是一个素数的非回文数。例如：17 和 71 都是素
# 数且都不是回文数，所以 17 和 71 都是反素数。请编写一个函数判断一个数是否是反
# 素数？并编写测试程序找出前 30 个反素数输出到屏幕上，要求每行输出 8 个数，每个
# 数占 5 列，右对齐。 




def assignment90(n):
    '''
    fucntion：判断这个数是不是反素数
    para：n---输入的整数，res---是不是反素数，是为True，不是为False
    return:res
    example:
        71 ===>True
        12 ===>False
        23 ===>False
    '''
    lst=list(str(n))
    lst1=lst[::-1]
    if lst1[0]=='0':
        lst1.remove('0')
    answer=''
    for i in lst1:
        answer+=i
    a=int(answer)
    flag1=False
    for i in range(2,n):
        if n%i==0:
            break
    else:
        flag1=True
    flag2=False
    for i in range(2,a):
        if a%i==0:
            break
    else:
        flag2=True
    if flag1==True and flag2==True:
        return True
    else:
        return False
    

    
    pass   #占位语句，添加代码后删除pass
    


if __name__ == '__main__':  
    print(assignment90(19))