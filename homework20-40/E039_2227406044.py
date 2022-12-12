#39题：从键盘输入 2 个正整数，比较两者大小，输出较大值。

def assignment39(x,y):
    '''
    功能：找整数x,y中的最大值
    参数： x,y表示两个整数
    返回值：x,y中较大值
    '''
    if x>=y:
        return x
    else:
        return y
   #占位语句，添加代码后删除pass

    

if __name__ == '__main__':
    #step1: 从键盘输入两个整数
    a,b =eval (input("输入两个数用逗号隔开")) 
    #step2: 
    result = assignment39(a,b)
    print("{0:d}和{1:d}的最大值是{2:d}".format(a,b,result))