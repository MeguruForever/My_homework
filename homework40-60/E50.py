# -*- UTF-8 -*-
'''
50题：
从键盘输入两个浮点数 x1 和 y1 作为圆心坐标，从键盘输入一个浮点数 r 作为半径，这
样就在 XOY 二维平面上唯一地确定了一个圆。再从键盘输入两个浮点数 x2 和 y2，编
写程序以判断坐标点(x2,y2)是在圆内还是在圆外（注：在圆周上也是在圆内），并显示
相应的判断结果。
'''

def assignment50(center,r,point):
    '''
    功能：判断坐标点与圆的位置
    参数：center---圆心坐标列表,[x坐标，y坐标]，示例：[0,0]
         r---圆半径
         point---XOY平面上的一点坐标列表，[x坐标，y坐标]，示例：[0,0]
    返回值：1---point在圆内，0---point圆外
    '''
    #step1: 计算point和center之间的距离d
    d=(((center[0]-point[0])**2)+((center[0]-point[1])**2))**(1/2)

    #step2: 比较d与r之间的关系，并返回比较结果。注意：d和r的比较方式
    if d>r:
        return "园外"
    elif d>=r:
        return "园内"
   #占位语句，添加代码后删除pass

    

if __name__ == '__main__':
    #step1: 从键盘输入圆心坐标
    center =list(map(float,input("圆心坐标").split(",")))
    #step2: 从键盘输入园半径
    r = float(input("半径"))
    #step3:从键盘输入点坐标
    point =list(map(float,input("输入坐标用逗号隔开 1,3 像这样").split(",")))
    #step4: 调用函数判断圆与点的位置关系
    result = assignment50(center,r,point)
    #step5: 根据step4输出位置关系描述
    print (result)