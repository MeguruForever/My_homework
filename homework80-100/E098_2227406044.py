# 编写一个程序，实现字符过滤。从键盘输入 2 个字符串，第一个是待过滤字符串，第二
# 个是过滤字符集合，将待过滤字符串按照过滤字符集合进行过滤，最后将过滤后的字符
# 串输出。例如带过滤字符串为 1+2=3，过滤字符集为+=，过滤结果为 123
def str_filter(input_str,filter):
    '''
    function:对输入的字符串按照过滤字符集进行过滤
    param：
        input_str:待过滤的字符串
        filter：过滤字符集合
        result:过滤后的字符串
    return：result
    example:
        input_str="1+2=3"
        filter="+=" 
        result="123"
    '''
    result=""
    for i in input_str:
        if i not in filter:
            result+=i
    return result

if __name__ == '__main__':
    input_str="1+2=3"
    filter="+="
    result=str_filter(input_str,filter)
    print(result)
