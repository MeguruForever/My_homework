nums=list(map(int,input("输入三位整数")))#将输入数加入列表
print (nums)
res=0#预存数res
for a in nums:#遍历nums 全部加上去
    res+=a
print ("答案是""%04.f"%res)