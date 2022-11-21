# -*- UTF-8 -*-
"""
题目：从键盘输入一个字母， 如果输入的是小写英文字母， 请将其转换为大写字母后显示输出；
如果输入的是大写英文字母，请将其转换为小写字母后显示输出；如果既不是小写英文
字母、也不是大写英文字母，则原样显示。
"""
#说明：此题本次作业可以不做，等讲完字符串再做

def assigment54(character):
    '''
    function: 字符大小写转换
    param: character--- 一个字母
    return: 转换的结果

    例子:
    character:A
    result:a

    character:$
    result:$
    '''
    
    if ord(character)>96 and ord(character)<123:
        return character.upper()
    elif ord(character)>64 and ord(character)<97:
        return character.lower()
    else:
        return character

if __name__ == '__main__':
    #输入一个字母
    char='a'
    result = assigment54(char)
    print(result)