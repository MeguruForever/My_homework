# 有一个元组，元组内存放若干整数。编写程序，统计元组中的元素个数，输出最大值、
# 最小值、平均值。





def assignment79(t):
    '''
    fucntion：统计输入元组中的个数、最大值、最小值、平均值
    para：t---输入的元组
    return:res---(个数(int)，最大值(int)，最小值(int)，平均值(float))
    Example: (10,9,11,10,10)===>(5,11,9,10.0)  
    '''
    lst=[]
    al=0
    for i in t:
        lst.append(i)
        al+=i
    a=len(lst)
    b=max(lst)
    c=min(lst)
    d=al/a
    return (a,b,c,d)
    
    #占位语句，添加代码后删除pass

    
if __name__ == '__main__':
    #输入一个存放若干整数的元组
    t = (10,9,11,10,10)
    

    result = assignment79(t)
    print(result)