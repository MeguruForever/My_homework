# 学校举办了“十佳歌手大赛”，有若干名选手参赛，7 名评委分别对这些选手进行了评分，
# 评分范围为 0~10。评分去掉最高分和最低分后取平均值，这个平均值将作为选手的最
# 终得分。编写程序，计算并输出这些选手的姓名和最终得分，得分保留一位小数。


def assignment73(lst):
    '''
    fucntion：去掉列表中的最高分和最低分求平均值
    para：lst---七名评委的评分，res---去掉列表中的最高分和最低分求平均值
    return:res
    Example: [7,8,8,8,8,8,9]===>8.0
    '''
    lst1=[]
    for i in lst:
        lst1.append(i)
    lst1.remove(max(lst))
    lst1.remove(min(lst))
    res=0
    for i in lst1:
        res+=i
    return res/5
    
    
    pass   #占位语句，添加代码后删除pass

    
if __name__ == '__main__':
    #七名评委的评分，评分范围为 0~10，存储在元组中，如(7,8,8,8,8,8,9)
    lst = (7,8,8,8,8,8,9)

    result = assignment73(lst)
    print(result)
  