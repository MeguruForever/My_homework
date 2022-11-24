#  编写一个函数实现选择排序。从键盘依次输入 10 个字母（如果有大小写，需要区分），
# 按照字母的 ASCII 码值分别进行从小到大、从大到小的排序，并输出排序的结果。

def assignment93(lst):
    '''
    fucntion：选择排序
    para：lst---输入的列表
    return:res1,res2  （元组类型）res1---c从小到大，res2 从大到小
    example:
        [15,78,23,4,6,85,65,42,12,36]===>res1: ['A', 'B', 'C', 'c', 'q', 'w'] res2: ['w','q','c','C','B','A']
    '''
    lst.sort()
    a=sorted(lst,reverse=True)
    return lst,a

        
    
    
    pass   #占位语句，添加代码后删除pass
    


if __name__ == '__main__':
    #从键盘输入10个整数，整理格式将其放在列表lst中，如[15,78,23,4,6,85,65,42,12,36]

    lst=["A","C","c","w","B","q"]
    result = assignment93(lst)
    print(result)