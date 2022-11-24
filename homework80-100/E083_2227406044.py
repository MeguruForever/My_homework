#  小明想在学校中请一些同学一起做一项问卷调查，请编程帮助小明解决如下问题：
# a) 用户输入 N； 
# b) 为了实验的客观性先用计算机生成 N 个 1～1000 之间的随机整数(N<=1000)； 
# c) 对于其中重复的数字，只保留一个，将其余相同的数字去掉，不同的数对应着不同
# 学生的学号；
# d) 然后再将这些数从小到大排序，按照排好的顺序去找同学做调查。输出排序的结果。



def assignment83(N):
    '''
    fucntion：生成N个1-1000之间的随机整数，去重并按从小到大的顺序排序
    para：N---N个学生
    return:lst---去重排序后的结果
    Example: 6===>[5,9,21,33,50,69](结果不唯一，符合规则即可)
    '''
    import random
    lst=[]
    lst2=[]
    for i in range(N):
        a=random.randrange(1,1001)
        lst.append(a)
    for i in lst:
        if i not in lst2:
            lst2.append(i)
    lst2.sort()
    return lst2
    pass   #占位语句，添加代码后删除pass

    
if __name__ == '__main__':
    #输入N
    N = 10
   

    result = assignment83(N)
    print(result)