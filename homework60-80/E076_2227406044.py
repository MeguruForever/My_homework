# 在程序中创建两个字典，找出并显示两个字典中具有相同值（要求数据类型也相同）的键。



def assignment76(dic1,dic2):
    '''
    fucntion：找出两个字典中值相同的对应键
    para：dic1,dic2---输入的两个字典，lst---两个字典中值相同的对应键，存储在列表中，排序后返回
    return:lst
    Example: 
        {'a':5,'b':8,'c':2},{'a':3,'b':10,'c':2}===>['c']
        {'a':5,'b':3,'c':2},{'a':5,'b':3,'c':2}===>['a','b','c'] 
    '''
    lst=[]
    for i in dic1:
        if dic1[i]==dic2[i]:
            lst.append(i)
    return lst   #占位语句，添加代码后删除pass

    
if __name__ == '__main__':
    #输入两个字典
    dic1 = {'a':5,'b':3,'c':2}
    dic2 = {'a':5,'b':3,'c':2}

    result = assignment76(dic1,dic2)
    print(result)