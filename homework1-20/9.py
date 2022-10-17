import random
num=random.randrange(100,999)
print (num)
num1=num//100
num2=num//10%10
num3=num%10#找出各个位上的数字
a=num3*100+num2*10+num1
print (format(a,'03d'))
