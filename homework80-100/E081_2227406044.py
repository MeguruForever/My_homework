#  设计一个购物小程序。有一组商品，名称和单价存放在一个字典中。编写程序，按照商
# 品名称排序输出商品选择菜单，内容包括序号、商品名称和单价。通过键盘输入序号，
# 输入商品序号则对应商品加入购物车，然后继续输入序号，直到输入 0 代表结算。结算
# 时显示购物车的所有商品信息，包括商品名称、单价、购买数量和小计金额，以及所有
# 购物车内商品的总价。

#step1 初始化商品的列表，以下变量均可自定义
goodlist=["cola","chips","pen","toy"]
procelist=[3, 5, 2, 10]
idlist=[0 ,1, 2, 3]
dic={}
#step2  利用元组，字典的方式将以上列表信息整合起来
for i in idlist:
    dic[i]=[goodlist[i],procelist[i]]
#step3 键盘输入序号
key=[]
while 0 not in key:
    key.append(int(input("序号")))

#step4  通过序号查找商品，并加入购物车，直到输入0代表结束
if 0 in key:
    num=[0,0,0,0]
    res=0
    for i in key:
        if i ==0:
            num[0]+=1
        elif i==1:
            num[1]+=1           
        elif i ==2:
            num[2]+=1
        elif i==3:
            num[3]+=1
        res+=dic[i][1]
for i in range(0,4):
    print(dic[i],num[i],num[i]*dic[i][1])
print(res)
#step5 结束后，显示所有购物车的信息  包括商品名称、单价、购买数量和小计金额，以及所有 购物车内商品的总价。