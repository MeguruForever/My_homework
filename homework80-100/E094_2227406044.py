# 94. 写一个程序，用户输入一个字符串 s，返回一个由 s 的前 2 个字符和后 2 个字符组成的
# 新字符串。如果 s 的长度小于 2，则返回空字符串。
# 例：输入'python'，返回'pyon'。

def parseString(input_str):
    '''
    function:对输入的字符串按照题意进行处理，返回一个新的字符串
    param:
        input_str:输入的字符串
        result：处理后的字符串
    return:result
    example:
        input_str : "python", result="pyon"
        input_str: "abc",  result="abbc"
        input_str: "a",   result=""
    '''
    if len(input_str)<2:
        result=""
    else:
        result=input_str[0:2]+input_str[-2:]
    return result


if __name__ == '__main__':
    input_str="python"
    result=parseString(input_str)
    print(result)