# 102. 编写一个函数，判断一个密码（用字符串表示）是否是好密码。一个好的密码满足：
# a) 长度不小于 8；
# b) 至少含有一个数字；
# c) 至少含有一个小写字母；
# d) 至少含有一个大写字母。
# 如果密码是好密码，返回 True，否则返回 False。
def good_password(password):
    '''
    function：判断是否为一个好密码
    param：
        password：输入的密码
        result：True：好密码，False：不是好密码
    return：result
    example：
        password: "123456789"
        result=False

        passoword: "Aa123456789"
        result=True
    '''
    if len(password)<8:
        result=False
    else:
        if password.islower() or password.isupper() or password.isdigit():
            result=False
        else:
            reslower=False
            resupper=False
            resdigit=False
            for i in password:
                if i.islower():
                    reslower=True
                elif i.isupper():
                    resupper=True
                elif i.isdigit():
                    resdigit=True
            if reslower and resupper and resdigit:
                result=True
    return result


if __name__ == '__main__':
    password='kjjkD123456789'
    result=good_password(password)
    print(result)