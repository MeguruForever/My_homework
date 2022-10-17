res=0
for i in  range (5):#五年的存款循环
    res+=100#先存一百
    res*=1.005#涨利息
    print (res)
print (format(res,'.5f'))
shouyi=(res-500)/500
print (format(shouyi,'.2%'))
