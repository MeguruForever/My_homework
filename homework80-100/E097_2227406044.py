# 97. 统计一个字符串中所有字符出现的次数。例：给定"google.com"，输出： 'o': 3, 'g': 2, '.': 1,
# 'e': 1, 'l': 1, 'm': 1, 'c': 1
def count_char(input_str):
    '''
    function:统计一个字符串中所有字符出现的次数
    param:
        input_str:输入的字符串
        result_dic:统计所有字符出现次数的字典
    return：result_dic
    example:
        input_str: "google.com"
        result_dic: { 'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}  ##返回的结果必须为字典类型
    '''
    result_dic={}
    lst=list(input_str)
    for i in lst:
        if i in result_dic.keys():
            result_dic[i]+=1
        else:
            result_dic[i]=1
    return result_dic


if __name__ == '__main__':
    input_str="google.com"
    result=count_char(input_str)
    print(result)