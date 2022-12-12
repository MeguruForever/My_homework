#37题：输入一个[0~100]的整数，判断这个数是否能被 3 整除，如果输入的数不在范围内提示错误信息。

def assignment37(num):
    if num>100 or num<0:
        return "输错了"
    if num%3==0:
        return True
    else:
        return False
    '''
    功能：判断整数num是否能被3整除
    参数：num表示整数
    返回值：若能被3整除返回True，否则返回False, 参数num超出范围返回None
    '''    
    #step1: 判断参数是否在指定返回，如果不在，直接返回None

    #step2: 判断参数是否能被3整数，如果能，返回True,否则返回False
    

  #占位语句，添加代码后删除pass



if __name__ == '__main__':
    #step1:输入一个整数
    num = int(input("输入一个整数"))
    #step2: 调用函数判断结果
    result = assignment37(num)
    
    print(result)