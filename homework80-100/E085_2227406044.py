# 使用 random 模块生成一个整数类型的随机数集合：生成 100 个[0,1000]范围内的随机
# 数。这些数字组成集合 A。同理，按此方法生成集合 B。在此基础上实现以下功能：
# a) 显示 A 和 B 的结果。要求每行最多显示 10 个数，每个数占 5 列，右对齐； 
# b) 要求用户输入 A|B 和 A&B 的结果，并告诉用户的答案是否正确。如果用户回答错
# 误，允许修改答案，然后重新验证用户输入的答案。如果用户三次提交的答案均不
# 正确，程序将显示正确结果
n=100
#step1:生成100个[0,1000]的随机整数组成集合A、B
import random
A = []
B = []
for i in range(n):
    a=random.randrange(0,1001)
    A.append(a)
for i in range(n):
    a=random.randrange(0,1001)
    B.append(a)
A=tuple(A)
B=tuple(B)

#step2:按照每行最多10个，每个数占5列，右对齐的格式打印A和B
count=0
for i in range(len(A)):
    print(format(A[i],'5d'),end='')
    count+=1
    if count%5==0:
        print()
count=0
for i in range(len(B)):
    print(format(B[i],'5d'),end='')
    count+=1
    if count%5==0:
        print()

#step3:要求用户输入A|B 和 A&B 的结果,若错误可以修改，最多输入3次，3次后输出正确结果
flag=False
count1=0
while flag==False:
    answer1=input('输入答案A|B')
    answer2=input('输入答案A&B')
    count1+=1
    if answer1==A[1]|B[1] and answer2==A[1]&B[1]:
        flag=True
        print('对')
    elif answer1==A[1]|B[1] and answer2!=A[1]&B[1]:
        print('A|B对,A&B错')
    elif answer1!=A[1]|B[1] and answer2==A[1]&B[1]:
        print('A|B错,A&B对')
    if count1==3:
        print(A[1]|B[1],A[1]&B[1])