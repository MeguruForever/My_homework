# -*- UTF-8 -*-
"""
41题：模拟系统登录。建立一个用户信息列表，内部存有若干组用户名和密码。随机生成一个
4 位数验证码，用户从键盘依次输入用户名、密码和验证码，将用户输入的结果和用户
信息列表以及校验码进行比较，如果用户名和密码不正确则输出提示“用户名或密码不
正确”，如果验证码不正确则提示“验证码有误”，如果全部正确提示“登录成功”。
"""
import random

#step1: 手动构建一个用户列表userInfolst,例如：[["Joy","abc123"],["Mary","1234"],....]
userInfolst=[['"Joy","abc123"'],['"Mary","1234"']]

#step2: 随机生成一个4位整数作为验证码
key=random.randint(1000,10000)
#step3: 用户输入用户名和密码
a=[input("请输入您的用户名和密码(用逗号隔开):")]
#step4: 向用户显示step2生成的验证码
print("您的验证码为{}".format(key))
#step5: 用户输入验证码
b=int(input("请输入您的验证码:"))
#step6: 对用户名和密码、验证进行验证，并给出验证结果
if a in userInfolst and b==key:
    print("登录成功")
elif a not in userInfolst:
    print("用户名或密码不正确")
else:
    print("验证码有误")

