names=["张飞","李大刀","李墨白","王老虎","雷小米"]
gaoshu=[78,92,84,84,92]
xiandai=[75,67,88,50,98]
al=[]
def helper(al):
    return [al[1],al[2]]#如果al【1】相等 就看下面一个
for i in range (len(names)):
    al.append([names[i],gaoshu[i],xiandai[i]]) 
al.sort(key=helper,reverse=True)
for x in range (5):
    print (al[x])