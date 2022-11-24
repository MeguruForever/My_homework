# 已知两个列表，一个列表存放姓，一个列表存放名。编写程序生成一个字典，字典的键
# 由姓和名构成，姓按列表顺序选取，名从列表中随机选择，字典的值使用[0-100]的随机
# 整数。将字典内值在 0-18 范围内的元素全部去除




def assignment77(lst1,lst2):
    import random
    '''
    fucntion：根据姓和名的列表生成一个名字，要按照姓的顺序来生成名字，然后以名字为键、0-100内的随机数为值生成一个字典，将字典中值为0-18内的键值对删除
    para：lst1---存放姓的列表，lst2---存放名的列表,dic---最后返回的字典
    return:dic
    Example: ['张','李','王'],['一','二','三','四'] ===>{'张三'：52，'李四':69,'王一':88}(结果不唯一，符合规定即可)
    '''
    dic={}
    dic1={}
    for i in lst1:
        a=random.randrange(0,101)
        b=random.randrange(0,len(lst2))
        dic[i+lst2[b]]=a
    for i in dic.keys():
        if dic[i]>18:
            dic1[i]=dic[i]    
    return dic   #占位语句，添加代码后删除pass

    
if __name__ == '__main__':
    #存放姓的列表，如['张','李','王']
    lst1 = ['张','李','王']
    #存放名的列表，如['一','二','三','四']
    lst2 = ['一','二','三','四']

    result = assignment77(lst1,lst2)
    print(result)