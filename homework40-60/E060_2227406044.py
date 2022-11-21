# -*- UTF-8 -*-
"""
题目：有一组人员的姓名和年龄数据，编写程序找到这组数据中年龄最大的人，输出相关人员信息
"""

def  getMaxAgePersonInfo(lstPerson):
    '''
    function: 查找年龄最大的人员信息
    parm: lstPerson---由[姓名，年龄]为元素构成的二维列表
    reval: 年龄最大的人员信息[姓名，年龄]
    '''
    def helper(x):
        return x[1]
    
    lstPerson.sort(key=helper,reverse=True)
    return lstPerson
    # 占位语句，完成函数后删除

if __name__=="__main__":
    #step1 编写一组list包含所有人员的姓名和年龄，例如datasets=[["Lisa",30],["Anna",20]]
    datasets=[["Anna",20],["Lisa",30]]
    print(datasets)
    #step2 查询这组数据年龄最大的一组，并且输出其信息
    lst = getMaxAgePersonInfo(datasets)
    print(lst)
