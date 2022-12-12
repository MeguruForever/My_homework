# 第38题：
# 从键盘上输入一个不多于 5 位的正整数，编写程序实现如下要求：
# （1）求出它是几位数；
# （2）分别输出每一位数字；
# （3）按逆序输出每位数字，例如原数为 321，应输出 123

def assignment38(num):
    '''
    功能：获取整数num的位数，各位数字和逆序整数
    参数: num:一个不多于 5 位的正整数
    返回值：[res1,res2,res3]
       res1: 表示整数的位数
       res2: 由整数各位数字组成的列表
       res3: 整数的逆序整数
       如果num不符合要求，则返回[None,None,None]
    示例：num=2345, 返回值：[4,[2,3,4,5], 5432]
          num=123456, 返回值:[None,None,None]
    '''
    if num >=1e6:
        return [None,None,None]
    res1=0
    res2=[]
    res3=0
    temp1=num
    while temp1>0:
        temp1//=10
        res1+=1
    temp2=num
    while temp2>0:
        a=temp2%10
        res3=(res3*10)+a
        temp2//=10
        res2.append(a)
    res2.reverse()
    return [res1,res2,res3]
 #占位语句，添加代码后删除pass


if __name__ == '__main__':
    #step1: 从键盘输入一个不多于 5 位的正整数
    num = int(input("输入一个不多于五位的正整数"))
    #step2: 获取整数num的位数，各位数字和逆序整数
    result = assignment38(num)

    print("{0:d}是{1:d}位整数".format(num,result[0]))
    print("{0:d}的各位数字是:".format(num),result[1])
    print("{0:d}的逆序整数是{1:d}".format(num,result[2]))