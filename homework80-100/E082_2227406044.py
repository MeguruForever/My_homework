# 创建一个有关雇员姓名和编号处理的程序。从键盘输入一组雇员姓名和编号。在此基础
# 上实现：
# a) 按照雇员姓名的顺序输出数据，雇员姓名显示在前面，后面是对应的雇员编号。
# b) 按照雇员编号的顺序输出数据，雇员编号显示在前面，后面是对应的雇员姓名


def assignment82(lst):
    '''
    fucntion：根据输入的雇员姓名和编号，实现题中的要求a和要求b
    para：lst---输入的一组雇员和编号信息
    return:[res1,res2] res1---要求a的结果,res2---要求b的结果
    Example: [('zhangsan',1),('lisi',3),('wangwu',2)]===>[[('lisi', 3), ('wangwu', 2), ('zhangsan', 1)], [(1, 'zhangsan'), (2, 'wangwu'), (3, 'lisi')]]
    '''
    lst1=[]
    for i in lst:
        temp=[]
        for j in i: 
            temp.insert(0,j)
        lst1.append(tuple(temp))
    return [lst,lst1]
    

    pass   #占位语句，添加代码后删除pass

    
if __name__ == '__main__':
    #从键盘输入一组雇员和编号，有很多输入方法，但是要求最后输入函数的格式为[('zhangsan',1),('lisi',3),('wangwu',2)]
    lst = [('zhangsan',1),('lisi',3),('wangwu',2)]
   

    result = assignment82(lst)
    print(result)