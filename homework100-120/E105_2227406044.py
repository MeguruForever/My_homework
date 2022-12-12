# 请利用正则表达式写一个简单的拼写检查程序。实现以下功能：
# a) 两个或两个以上的空格出现时将其压缩为一个。
# b) 在标点符号后加上一个空格，如果这个标点符合之后还有字母。
# 例： 给定字符串："Thisisvery funny andcool.Indeed!" 
# 输出："This is very funny and cool. Indeed!" 
# 其中“ ”代表一个空格

import re
def spellChecking(input_str):
    '''
    function:对输入的英文字符串进行格式检查，返回正确的格式
    param:
        input_str:输入的英文字符串
        res:正确格式的字符串
    return:res
    example:'How    are you?Fine.'==>'How are you? Fine.'
    '''
    #利用正则表达式进行格式检查
    input_str=re.sub(r'\s+',' ',input_str)
    input_str=re.sub(r'([,.!;:/?])',r'\1 ',input_str)
    return input_str
    

if __name__ == '__main__':
    input_str ='How    are you?Fine.'
    res = spellChecking(input_str)
    print(res)