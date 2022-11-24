# -*- UTF-8 -*-
"""
题目：有一条地铁线一共有 30 个站点，这些站点编号为 0~29,已知所有相邻站点间的距离，
distance[i]表示编号为 i 的车站到编号为 i+1 车站间的距离，单位为 km，站距均在
1.5km~3.0km 间。假设地铁的车票和距离有关，基础票价为 2 元(5km 内)，超过 5km 后
每 5km 增加 1 元（不满 5km 的部分按 1 元计算）。编写一个程序，计算花 n 元最多能
乘坐多少站(站数不包括起点站，包括终点站)。
"""
 

def assginment64(distances,money):
    result=0
    '''
    function: 根据站点间的距离和钱计算能坐的站数
    param: distances --- 表示地铁线站之间的距离列表，distance[i]表示编号为 i 的车站到编号为 i+1 车站间的距离
    money: 拥有的钱
    reval: 最多能乘多少战    
    例子1：
    distances=[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
    money=2
    count=2 ; distances中的[3,2]或者[2,3]两站
    例子2：
    distances=[3, 3, 3, 1.5, 1.5, 2, 3, 3, 3, 3, 3, 3, 3, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
    money=3
    count=4 ; distances中的[1.5, 1.5, 2, 3]
    '''
    if money <2:
        return 0
    mile=5
    money-=2
    while money>=1:
        money-=1
        mile+=5
    lst=[]
    for x in range (len(distances)):
        mile1=mile
        count=0
        for i in range (x,len(distances)):
            mile1 -= distances[i]
            count+=1
            if mile1 <0:
                lst.append(count-1)
                break
    return max(lst)
            
        
    
    
if __name__ == '__main__':
    distances=[3, 3, 3, 3, 3, 1.5, 1.5, 3, 3, 3, 3, 3, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
    #step1: 产生[1,15]的随机整数
    money= 10
    result=assginment64(distances,money)
    print("{0:3d}元最多能乘坐的车站数:{1:3d}".format(money,result))