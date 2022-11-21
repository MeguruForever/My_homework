# -*- UTF-8 -*-
"""
题目：一块球拍售价 15 元,球 3 元,水 2 元。现在有 N 元，要求每种商品至少购买一个,有多
少种可能正好把这 N 元花完?
"""

def assignment56(N):
    #参数：N 表示N元钱
    #返回：res:共多少种可能正好花完
    #示例：N=200 ==> 204
    res=0
    N-=20
    for i in range(0,N//15+1):
        for x in range (0,(N-15*i)//3+1):
            for y in range (0,(N-15*i-3*x)//2+1):
                a=N-(i*15)-(x*3)-(y*2)
                if a==0:
                    res+=1

    return res
if __name__ == '__main__':
    #输入N元钱
    N = 200
    result = assignment56(N)
    print(result)