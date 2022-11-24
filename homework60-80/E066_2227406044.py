# 提示用户输入一个整型数字 n（ n 代表后续需要输入整型数的数量），将 n 个整型数加起
# 来并输出，如果输入的是非整型数则提示当前的输入非法，需要重新输入数值，如果输
# 入‘ n=0’代表退出程序，否则继续提示用户输入新的 n。
#
# 例：
# Please input the number of numbers： （假设输入3）
# Please input number 1： (假设输入 3)
# Please input number 2： (假设输入 4)
# Please input number 3： (假设输入 5)
# 输出： sum = 12
# Please input the number of numbers：
# …
# Please input the number of numbers： （假设输入0，则退出程序）
n=int(input('输入一个整型数字'))
if n==0:
    exit()
res=0
for i in range (n):
    try:
        a=int(input('输入一个整型数字'))
        res+=a
    except:
        print("错误")
        exit()
print (res)
    
