# 设计一个用户注册程序，需要输入用户名、密码、确认密码三部分。这三部分分别有以
# 下要求：
# a) 用户名：长度大于等于 6，不能以数字开头，不能包含!？@等符号，-除外。
# b) 密码：长度大于等于 6，只能使用数字、大写英文字母和小写英文字母，且必须同
# 时使用这 3 种字符。
# c) 确认密码：要求与密码相同，除此之外确认密码需要和密码完全一致。
# 依次输入这三部分，如果输入正确输入下一项，如果错误则提示，然后重新输入该项内
# 容。
#让用户输入用户名，满足要求进入下一部分
flag1=False
while flag1==False:
    username=input('请输入用户名：')
    if len(username)<6:
        print('用户名长度必须大于等于6')
    elif username[0].isdigit():
        print('用户名不能以数字开头')
    elif '!' in username or '?' in username or '@' in username:
        print('用户名不能包含!?@等符号，-除外')
    else:
        flag1=True
#让用户输入密码，满足要求进入下一部分
flag2=False
while flag2==False:
    password=input('请输入密码：')
    lst=list(password)
    fuhao=False
    digit=False
    upper=False
    lower=False
    for i in lst:
        if i.isdigit()==False and i.isupper()==False and i.islower()==False:
            fuhao=True
        if i.isdigit():
            digit=True
        elif i.isupper():
            upper=True
        elif i.islower():
            lower=True
    if len(password)<6:
        print('密码长度必须大于等于6')
    elif digit==False or upper==False or lower==False:
        print('密码必须同时使用数字、大写英文字母和小写英文字母')
    elif fuhao==True:
        print('密码只能使用数字、大写英文字母和小写英文字母')
    else:
        flag2=True

#让用户输入确认密码，满足要求进入下一部分
    flag3=False
    if flag2==True:
        while flag3==False:
            password2=input('请再次输入密码：')
            if password2==password:
                flag3=True
            else:
                print('两次密码不一致，请重新输入')
            if flag1==True and flag2==True and flag3==True:
                print('注册成功')
                break