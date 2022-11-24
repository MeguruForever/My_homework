#71题：编写一个程序，有一个元组，内部有重复的若干元素，将重复元素去除后存入新的列表中。


def assignment71(t):
    '''
    fucntion：将元组内的元素去重，存入新的列表中
    para：t---有重复元素的元组，lst---去重后的列表
    return:lst
    Example: (1,1,1,2,2,3,4)===>[1,2,3,4]
    '''
    lst=[]
    for i in t:
        if i not in lst:
            lst.append(i)
    return lst    
#占位语句，添加代码后删除pass

    
if __name__ == '__main__':
    #输入一个元组
    t = (1,1,1,2,2,3,4)

    result = assignment71(t)
    print(result)
  