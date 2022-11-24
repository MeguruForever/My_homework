# -*- UTF-8 -*-
"""
题目：输出一个乘法表。要求输入一个整数 n，输出 n*n 的乘法表，乘法表打印出来为下三
角样式，格式工整。例： 输入 n=4。输出：
1 2 3 4
1 1
2 2 4
3 3 6 9
4 4 8 12 16
"""
n=int(input("输入n"))
for m in range (1,n+1):
  print (m,end='\t')  
print ('')
print ('')
for g in range (1,n+1):
  print(g,end='\t') 
  for u in range (1,n+1):
    print (g*u,end='\t')
    if u==g:
      break
  for o in range (2):
    print('')
