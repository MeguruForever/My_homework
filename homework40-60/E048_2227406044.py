# -*- UTF-8 -*-
'''
48题：从键盘分别输入 3 个 XOY 二维平面内某三角形的顶点坐标（6 个浮点数），在此基础上
计算三角形的面积和周长。如果不能构成三角形需要提示错误信息。
'''

def assignment48(lstPoint):
    '''
    功能：根据三角形三个顶点的坐标，计算三角形面积和周长
    参数：lstPoint---三个顶点坐标列表，每个顶点坐标是一个列表，参数示例：[[0,1],[2,3],[4,5]]
    返回值：面积和周长构成的列表,[面积，周长]
    '''    
    a=(((lstPoint[0][0]-lstPoint[1][0])**2)+((lstPoint[0][1]-lstPoint[1][1])**2))**(1/2)
    b=(((lstPoint[0][0]-lstPoint[2][0])**2)+((lstPoint[0][1]-lstPoint[2][1])**2))**(1/2)
    c=(((lstPoint[1][0]-lstPoint[2][0])**2)+((lstPoint[1][1]-lstPoint[2][1])**2))**(1/2)
    Zc=a+b+c
    p=(a+b+c)/2
    s=(p*(p-a)*(p-b)*(p-c))**(1/2)
    if a+b<=c:
        return "no"
    elif a+c<=b:
        return "no"
    elif b+c<=a:
        return "no"
    else:
        return [float(s),float(Zc)]
    pass   #占位语句，添加代码后删除pass

    

if __name__ == '__main__':
    #step1:输入三个点坐标，并构成一个包含3个元素的二维列表
    lstPoint = []
    while len(lstPoint)<3:
        lst=list(map(int,input("输入坐标用逗号隔开 1,3 像这样").split(",")))
        lstPoint.append(lst)
    #step2:调用计算三角形面积和周长
    result = assignment48(lstPoint)
    print(lstPoint)
    try:
        print("面积为:{0:.4f},周长为:{1:.4f}".format(result[0],result[1]))
    except:
        print ("不是三角形")