#  有一个列表，存有若干英文单词。遍历整个列表，将这些单词按照首字母进行分类，存
# 储在字典中，最后输出这个字典。例如列表为["alpha","all","dig","date","egg"]，字典为
# {"a":["alpha","all"],"d":["dig","date"],"e":["egg"]}


def assignment72(lst):
    '''
    fucntion：将列表按照首字母进行分类，存储在字典中
    para：lst---含有若干英文单词的列表，dic---按照首字母分类的字典
    return:dic
    Example: ["alpha","all","dig","date","egg"]===>{"a":["alpha","all"],"d":["dig","date"],"e":["egg"]}
    '''
    dic={}
    for i in lst:
        lst1=list(i)
        dic[lst1[0]]=[]
    for i in lst:
        lst1=list(i)
        dic[lst1[0]].append(i)
            
    
    return dic   #占位语句，添加代码后删除pass

    
if __name__ == '__main__':
    #输入一个英文单词的列表，如["alpha","all","dig","date","egg"]
    lst = ["alpha","all","dig","date","egg"]

    result = assignment72(lst)
    print(result)
  