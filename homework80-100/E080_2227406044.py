#  有两个元组，一组存放了姓名，一组存放了年龄。将两组数据进行合并形成一个字典，
# 并输出。


def assignment80(t1,t2):
    '''
    fucntion：将两个元组按照顺序进行合并构成一个字典
    para：t1,t2---输入的两个元组，dic---合并后的字典
    return:dic
    Example: ('张三','李四','王五'),(20,21,22)===>{'张三':20,'李四':21,'王五':22}
    '''
    dic={}
    for i in range(len(t1)):
        dic[t1[i]]=t2[i]
    return dic
        
        
    
    pass   #占位语句，添加代码后删除pass

    
if __name__ == '__main__':
    #存放姓名的元组（两个元组的长度相同）
    t1 = ('张三','李四','王五')
    #存放年龄的元组
    t2 = (20,21,22)
   

    result = assignment80(t1,t2)
    print(result)