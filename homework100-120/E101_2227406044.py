# 101. 英语语法中，动词的第三人称单数形式规则简要概括（不完全）如下：
# a) 如果动词以 y 字母结尾，则去掉 y 并加上 ies。
# b) 如果动词以 o， ch， s， sh， x， z 字母结尾，则加上 es。
# c) 默认直接在动词最后加上字母 s。
# 请编写一个程序，对于任意给定的一个动词，返回其第三人称单数形式

def convert_third_person(word):
    '''
    function：为动词添加第三人称单数
    param:
        word:输入的动词
        result：添加第三人称单数形式后的动词
    return：result
    example：
        word: "study"
        result: "studies"
    '''
    if word[-1]=='y':
        result=word[:-1]+'ies'
    elif word[-1] in ['o','s','x','z']:
        result=word+'es'
    elif word[-2:] in ['ch','sh']:
        result=word+'es'
    else:
        result=word+'s'   
    return result


if __name__ == '__main__':
    word="schp"
    result=convert_third_person(word)
    print(result)
