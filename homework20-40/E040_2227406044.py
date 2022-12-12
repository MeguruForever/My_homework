# 从键盘输入任意 3 个整数，按从小到大的顺序输出

def assignment40(x,y,z):
    '''
    功能：对三个整数按从小到大排序
    参数：x,y,z 表示三个整数
    返回值：[a,b,c]:x,y,z按从小到大排序构成的列表
    返回值示例：x=5,y=8,z=2, [2,5,8]
    '''
    list1=[]
    list1.append(x)
    list1.append(y)
    list1.append(z) 
    list1.sort()
    return list1
    #占位语句，添加代码后删除pass

    

if __name__ == '__main__':
    #step1: 从键盘输入三个整数
    x,y,z = eval (input("输入三个数"))
    #step2: 调用函数获得三个整数的升序排序列表
    result = assignment40(x,y,z)
    print(result)