# 95. 写一个程序处理用户输入的字符串，并按用户要求删除其中第 n 个字符，返回删除字符
# 后的字符串。
def delete_n_char(input_str,n):
    '''
    function：删除输入字符串中第n个字符，返回新的字符串，假设n小于等于字符串长度
    param:
        input_str:输入的字符串
        n:删除第n个字符
        result:返回的结果
    return：result
    example:
        input_str: "abc" n:2
        result="ac"

        input_str="hellow wolrd"  n:3
        result="helow wolrd"

    '''
    if n>=len(input_str):
        return input_str
    result=input_str[0:n-1]+input_str[n:]
    return result


if __name__ == '__main__':
    input_str="abc"
    n=2
    res = delete_n_char(input_str,n)
    print(res)