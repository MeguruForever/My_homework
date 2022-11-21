# -*- UTF-8 -*-
"""
题目：从键盘输入一批学生的成绩（成绩为整数），输入 0 或负数则输入结束，然后统计并输
出优秀（大于等于 90）、通过（ 60～59）和不及格（小于 60）的人数。
"""

def getGradOfStudents(lst):
    '''
    function: 根据学生成绩列表lst，统计优秀人数、通过人数和不及格人数
    para: lst---学生成绩列表
    return: [优秀人数，通过人数，不及格人数]
    '''
    youxiu=0
    tongguo=0
    bujige=0
    for i in lst:
        if i >=90:
            youxiu+=1
        elif i<90 and i>=60:
            tongguo+=1
        else:
            bujige+=1
    return [youxiu,tongguo,bujige]
            # 占位语句，完成函数后删除

if __name__ == "__main__":
    #step1:学生成绩输入控制(参考循环一章的ppt中循环控制方式)
    flag=True
    lst=[]
    while flag == True:
        #step1.1: 学生成绩输入
        a=int(input('输入成绩'))
        #step1.1: 判断成绩是否应该保存还是输入结束
        if a>0:
            lst.append(a)
        elif a<=0:
            break
        
        

    #step2: 调用函数getGradOfStudents()统计学生成绩分布情况
    lstGrad = getGradOfStudents(lst)

    #step3: 输出优秀人数
    print (lstGrad[0])
    #step4: 输出通过人数

    print (lstGrad[1])
    #step5: 输出不及格人数
    
    print (lstGrad[2])