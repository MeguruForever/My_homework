# -*- UTF-8 -*-
'''
49题：
从键盘分别输入 3 个 XOY 二维平面内某三角形的顶点坐标（6 个浮点数），判断该三角
形是等边三角形、直角三角形或其它三角形（不属于上述两种）中的哪一种。如果不能
构成三角形需要提示错误信息。
'''

def assignment49(lstPoint):
    '''
    功能：根据三角形三个顶点的坐标，判断三角形的特点
    参数：lstPoint---三个顶点坐标列表，每个顶点坐标是一个列表，参数示例：[[0,1],[2,3],[4,5]]
    返回值：1---等边三角形，2---直角三角形，3---其它三角形， None---不能构成三角形
    '''    
    #step1: 计算三角形三条边长d1,d2,d3

    #step2: 根据d1,d2,d3之间的关系判断三角形特征，并根据要求返回结果
    a=(((lstPoint[0][0]-lstPoint[1][0])**2)+((lstPoint[0][1]-lstPoint[1][1])**2))**(1/2)
    b=(((lstPoint[0][0]-lstPoint[2][0])**2)+((lstPoint[0][1]-lstPoint[2][1])**2))**(1/2)
    c=(((lstPoint[1][0]-lstPoint[2][0])**2)+((lstPoint[1][1]-lstPoint[2][1])**2))**(1/2)
    if a+b<=c:
        return "不能构成三角形"
    elif a+c<=b:
        return "不能构成三角形"
    elif b+c<=a:
        return "不能构成三角形"
    if a==b and b==c :
        return "等边三角形"
    elif a**2+b**2==c**2:
        return "直角三角形"
    elif a**2+c**2==b**2:
        return "直角三角形"
    elif b**2+c**2==a**2:
        return "直角三角形"
    else:
        return "其他三角形"
   #占位语句，添加代码后删除pass
    
if __name__ == '__main__':
    #step1: 输入三个点坐标，并构成一个包含3个元素的二维列表
    lstPoint = []
    while len(lstPoint)<3:
        lst=list(map(int,input("输入坐标用逗号隔开 1,3 像这样").split(",")))
        lstPoint.append(lst)
    #step2: 调用函数判断三角形特征
    result = assignment49(lstPoint)
    #step3: 根据result，输出特征描述信息：1---等边三角形，2---直角三角形，3---其它三角形， None---不能构成三角形
    print (result)