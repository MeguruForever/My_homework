#  请利用正则表达式写一个 Python 程序以尝试解析 XML/HTML 标签。现有如下一段内
# 容：
# <composer>Wolfgang Amadeus Mozart</composer> 
# <author>Samuel Beckett</author> 
# <city>London</city> 
# 希望自动格式化重写为：
# composer: Wolfgang Amadeus Mozart 
# author: Samuel Beckett 
# city: London

def parseXML(contents):
    '''
    function:解析XML文件，将内容写入字典中
    param:
        contents:XML/HTML标签内容
        dic:存放解析结果的字典
    return：dic
    example:
        '<composer>Wolfgang Amadeus Mozart</composer><author>Samuel Beckett</author><city>London</city>' 
        ==> {'composer':'Wolfgang Amadeus Mozart','author':'Samuel Beckett','city':'London'}
    '''
    import re
    res_dic = {}
    #利用正则表达式解析XML文件
    res= re.findall(r'<(\w+)>(.*)</\1>',contents)
    res_dic = dict(res)
    return res_dic





if __name__ == '__main__':
    contents = '<composer>Wolfgang Amadeus Mozart</composer> <author>Samuel Beckett</author> <city>London</city> '
    #解析XML文件并将其结果存入字典中
    res_dic = parseXML(contents)
    #根据字典内容逐行打印结果
    for i in res_dic:
        print(i+':'+" "+res_dic[i])
    
