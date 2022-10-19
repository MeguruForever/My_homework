names=["张飞","李大刀","李墨白","王老虎","雷小米"]
gaoshu=[78,92,84,50,99]
xiandai=[75,67,88,50,98]
al=[]
def helper(zongfen):#定义一个key函数 可以用来排序 返回排序的数字在列表的哪里
    return zongfen[1]
for i in range(len(names)):
    zongfen=gaoshu[i]+xiandai[i]
    al.append([names[i],zongfen])
al.sort(key=helper,reverse=True)
for x in range(4):#分行输出
    print (al[x])


