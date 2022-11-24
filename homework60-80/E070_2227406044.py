#70题：现在 8 名体检人员的体重信息如下(65.5,70.2,100.5,45.5,88.8,55.5,73.5,67.8)，请编写程序
#计算出方差


def assignment70(lst):
    '''
    fucntion：计算8名体检人员的体重方差
    para：lst---8名体检人员的体重信息,res---方差
    return:res
    '''
    al=0
    for i in lst:
        al+=i
    envy=al/len(lst)
    al2=0
    for i in lst:
        al2+=(i-envy)**2
    return al2/8
    #占位语句，添加代码后删除pass
    
if __name__ == '__main__':
    #8名体检人员的体重信息
    lst = (65.5,70.2,100.5,45.5,88.8,55.5,73.5,67.8)

    result = assignment70(lst)
    print(result)
