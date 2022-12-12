from calendar import c


nums=list(map(int,input("输入四个整数：").split( )))
a=nums[0]#取数
b=nums[1]
c=nums[2]
d=nums[3]
if a>=b:#两两比较找大数
   f=a
else:f=b
if c>=d:
   g=c
else:g=d
if f>=g:
   print(f)
else:print (g)

