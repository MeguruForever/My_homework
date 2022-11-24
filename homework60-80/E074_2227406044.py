#从键盘上随机输入若干个大写英文字母，编写程序使用字典统计所输入的每个字母出现的次数

def assignment74(chara):
    '''
    fucntion：统计从键盘上输入的若干大写英文字母中各个字母出现的次数
    para：chara---从键盘上输入的若干大写字母，dic---每个字母出现的次数，存储在字典中
    return:dic
    Example: "ABBCCC"===>{"A":1,"B":2,"C":3}
    '''
    dic={}
    lst1=list(chara)
    for i in lst1:
        if i not in dic:
            dic[i]=0
        if i in dic:
            dic[i]+=1
    return dic    
    
    

    pass   #占位语句，添加代码后删除pass

    
if __name__ == '__main__':
    #从键盘上输入的若干大写英文字母
    chara = input("输入若干大写英文字母")

    result = assignment74(chara)
    print(result)