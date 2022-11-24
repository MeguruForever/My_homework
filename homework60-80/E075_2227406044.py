#在程序中创建两个字典，找出并显示两个字典中相同的键。

def assignment75(dic1,dic2):
    '''
    fucntion：找出两个字典中相同的键，
    para：dic1,dic2---输入的两个字典，lst---两个字典中相同的键，存储在列表中，排序后返回
    return:lst
    Example: {'a':1,'b':2,'c':2},{'a':2,'b':1}===>['a','b']
    '''
    lst1=[]
    lst=[]
    for i in dic1.keys():
        lst1.append(i)
    for i in dic2.keys():
        if i in lst1:
            lst.append(i)
        
    return lst   #占位语句，添加代码后删除pass

    
if __name__ == '__main__':
    #输入两个字典
    dic1 = {'a':1,'b':2,'c':2}
    dic2 = {'a':2,'b':1}

    result = assignment75(dic1,dic2)
    print(result)