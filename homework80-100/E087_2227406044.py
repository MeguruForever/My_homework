# 编写一个程序，输入一个字符串，然后显示一个选择菜单，选 1 英文字符全部转换为大
# 写，选 2 小写英文字符全部转换为大写，最后将结果输出。

def assignment87(s,mode=True):
    '''
    fucntion：根据输入模式，将字符串转化为大写或小写
    para：s---输入的字符串,mode---模式，True表示转换为大写,False表示转换为小写
    return:res---输出的结果
    example:
        'abCDefG',1===>'ABCDEF'
        'abCDefG',2===>'abcdef'
    '''
    if mode==True:
        a=s.upper()
    if mode==False:
        a=s.lower()
    return a

    
    pass   #占位语句，添加代码后删除pass
    


if __name__ == '__main__':
    #输入的字符串
    s = 'abCDefG'
    
    result = assignment87(s,False)
    print(result)
    result = assignment87(s)
    print(result)