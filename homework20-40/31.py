a=list(input("输入一串字符"))
b=list(input("输入另一串字符"))
a.sort()
b.sort()
if a==b:
    print("同构")
else:print("不同构")