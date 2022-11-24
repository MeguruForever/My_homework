#  编写一个函数实现冒泡排序。从键盘输入依次输入 10 个整数，分别按照从小到大、从
# 大到小进行排序，并分别输出排序后的结果。




def assignment92(lst):
    '''
    fucntion：冒泡排序
    para：lst---输入的列表
    return:排序后的列表
    example:
        [15,78,23,4,6,85,65,42,12,36]===>[4, 6, 12, 15, 23, 36, 42, 65, 78, 85]
    '''
    for i in range(len(lst)-1):
        for j in range(len(lst)-i-1):
            if lst[j]>lst[j+1]:
                temp=lst[j]
                lst[j]=lst[j+1]
                lst[j+1]=temp
    return lst
        
    
    
    pass   #占位语句，添加代码后删除pass
    


if __name__ == '__main__':
    #从键盘输入10个整数，整理格式将其放在列表lst中，如[15,78,23,4,6,85,65,42,12,36]
    

    lst = [15,78,23,4,6,85,65,42,12,36]

    result = assignment92(lst)
    print(result)