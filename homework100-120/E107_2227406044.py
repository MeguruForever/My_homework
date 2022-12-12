# 编写程序，从键盘输入一个字符串，判断是否是电话号码，且输出号码的类型。判断要
# 求如下：
# a) 手机号码：长度 11 位的数字、并且以 1 开头
# b) 国内固定电话：区号长度 3 或 4 位且以 0 开头，电话号码长度 7、8 位且不以 0 开
# 头。区号和电话号码之间可以有-符号连接。
# c) 特殊号码：110、119、120 等。


def isPhoneNumber(input_str):
    '''
    function:判断键盘输入字符串是否为电话号码，若是输出电话的类型
    param:
        input_str:键盘输入的字符串
        res:判断的结果,具体结果见示例
    return:res
    exapmle:
        '1234567891011'==>[False]
        '13556954367'==>[True,'手机号码']
        '0512-6523695'==>[True,'国内固定电话']
        '120'==>[True,'特殊号码']
    '''
    res=0
    #判断是否为手机号码
    if len(input_str)==11 and input_str[0]=='1':
        res=[True,'手机号码']
    else:
        res=[False]
    #判断是否为国内固定电话
    lst1=input_str.split('-')
    if lst1[0][0]=='0' and len(lst1[0]) in (3,4) and lst1[1][0]!='0' and len(lst1[1]) in (7,8):
        res=[True,'国内固定电话']
    if input_str in ('110','119','120'):
        res=[True,'特殊号码']
    return res


if __name__ == '__main__':
    #输入字符串
    input_str = '12011111111'
    #调用函数判断是否为电话号码，若为电话号码判断其类型
    res = isPhoneNumber(input_str)
    if res[0]:
        print(input_str,'是',res[1])
    else:
        print(input_str,'不是一个电话号码')