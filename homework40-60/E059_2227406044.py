# -*- UTF-8 -*-
"""
题目：用 * 输出一个正六边形，输入一个整数 n 代表输出的正六边形的边的长度(*的数目)。
"""
n=int(input('输入边长'))
blank_upon=n-1
for i in range(n):
    print (' '*blank_upon,end='')
    blank_upon-=1
    print ('*'*(n+2*i))
blank_down=1
for j in range (n-1,0,-1):
    print (' '*blank_down,end='')
    blank_down+=1
    print ('*'*((n-2)+2*j))
#说明：这个输出图形在控制台如果不像图形那种对齐，只要空格个数符合要求，就可以认为是正确的，
# 因为控制台的显示不一定满足要求

