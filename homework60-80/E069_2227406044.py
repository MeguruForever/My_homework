# -*- UTF-8 -*-
"""
题目：有一个弹性小球从 H(H>=100)米的高度做自由落体运动，每次落地后会反弹，反弹高度
为上次下落高度的一半，然后继续下落，如此反复（假设反弹和下落不会停止）；编写
程序，计算并输出小球第 N 次落地时，共经过了多少米，第 N 次反弹的高度为多少。
"""


def assignment69(H,N):
    '''
    功能: 判断从高度H米进行自由落体运动,经过N次落地后共经过了多少米,第N次的高度为多少
    参数: H---表示高度; N---表示反弹次数
    返回值：[total,height]---total表示共经过了多少米, height表示第N次的高度
    返回值示例: H=100,N=5, [196.875,3.125]
    '''
    total=0
    for i in range (N):
        if i==0:
            total+=H
        else:
            total+=2*H
        H/=2
    return (total,H) 
        

    pass   #占位语句，添加代码后删除pass



if __name__ == "__main__":
    # step1:输入高度和反弹次数N的值
    H,N = 100,5
    # step2:调用函数输出结果
    result = assignment69(H,N)
    print(result)

