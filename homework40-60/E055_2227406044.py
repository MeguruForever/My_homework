# -*- UTF-8 -*-
"""
题目：给定一个二进制字符串，例如“ 10100101”，计算并输出字符串中 0 的个数以及所有数
字之和。
"""
#说明：此题本次作业可以不做，等讲完字符串再做


def assignment55(binary):
    num=0
    sum_num=0
    '''    
    :param binary: 二进制字符串 
    :return: num：0的个数，sum_num:所有数字之和
    
    例子: binary:"10100101"
    num:4 ,sum_num:4    
    '''
    lst=list(binary)
    for i in lst:
        if i=='1':
            num+=1
        sum_num+=int(i)
    return num,sum_num

if __name__ == '__main__':
    num,sum_num=assignment55("10100101")
    print("0的个数是",num)
    print("所有数字之和",sum_num)