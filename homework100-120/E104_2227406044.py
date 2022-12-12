#  一个字符串如果正读和反读都一样，那么它就是一个回文串。编写一个函数，判断一个
# 字符串在下列规则下是否是回文串：1）忽略所有空格；2）忽略所有的句号、逗号、感
# 叹号；3）不区分大小写。如果是回文串，返回 True，否则返回 False。

def isPalindrome(input_str):
    '''
    function:判断是否为回文串
    param:
        input_str:输入的字符串
        res:判断结果，True为回文，False不是回文
    return:res
    example:
        'ab,b a' ==> True
        'ab b' ==> False
        'ABCcba' ==> True
    '''
    #按照规则提取字符串
    lst1=list(input_str)
    lst2=[]
    for i in lst1:
        if i!=' ' and i!='.' and i!=',' and i!='!':
            lst2.append(i)
    if lst2==lst2[::-1]:
        return True
    else:
        return False

    #判读提取的字符串是否为回文

    pass


if __name__ == '__main__':
    input_str = 'ab,b a'
    res = isPalindrome(input_str)
    print(res)