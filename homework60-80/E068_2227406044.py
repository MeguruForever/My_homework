# -*- UTF-8 -*-
"""
题目：矩阵相加：提示用户输入一个数字 n，为矩阵的行数，再提示用户输入一个数字 m，为
矩阵的列数，接下来，提示用户输入 2*n*m 个数字（每次输入一个数字）。输出 C=A+B。
提示：思考怎么用 Python 实现二维数组（如果做矩阵相加没有问题了，可以思考如何
做矩阵相乘）。
Please input the number of rows：（假设输入 n=2） 
Please input the number of columns：（假设输入 m=3） 
Please input A[0,0]: 1 
Please input A[0,1]: 1 
Please input A[0,2]: 1 
Please input A[1,0]: 1 
Please input A[1,1]: 1 
Please input A[1,2]: 1 
Please input B[0,0]: 2 
Please input B[0,1]: 2 
Please input B[0,2]: 2 
Please input B[1,0]: 2 
Please input B[1,1]: 2 
Please input B[1,2]: 2 
输出：C = [[3, 3, 3], [3, 3, 3]]
"""




def assignment68(matrix2D1, matrix2D2):
    '''
    功能：计算两个矩阵的和
    参数: matrix2D1和matrix2D2---两个二维列表，表示二维矩阵
    返回值: 两个矩阵的和
    返回值示例: matrix2D1=[[1,1],[1,1]], matrix2D2=[[2,2],[2,2]]==>[[3,3],[3,3]]
    '''
    C=[]
    for i in range (len(matrix2D1)):
        lst1=[]
        for j in range (len(matrix2D1[i])):
            a=matrix2D1[i][j]+matrix2D2[i][j]
            lst1.append(a)
        C.append(lst1)    
    return C
    pass   #占位语句，添加代码后删除pass


if __name__ == "__main__":
    # step1:提示用户输入n和m，分别表示矩阵的行数和列数
    n,m = 2,3

    # step2:提示用户依次输入n*m个数,构成第一个矩阵
    matrix1=[[1,1],[1,1]]
    # step3:提示用户依次输入n*m个数,构成第二个矩阵
    matrix2=[[2,2],[2,2]]
    # step3:调用函数输出C=A+B
    result = assignment68(matrix1, matrix2)
    print('C=',result)