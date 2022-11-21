'''
第44题：
制作一个确认对话框，如下：
Confirm？(Y[es] or N[o]) 
从键盘输入内容，如果输入为 Y 或 Yes 或 YES 或 yes，则输出“Confirmed”；如果输入
为 N 或 No 或 NO 或 no，则输出“Not Confirmed”；输入其他内容则输出“输入错误”。
'''

def assignment44(inCMD):
    '''
    功能：根据输入的指令，返回对应的响应
    参数：inCMD--输入指令
    返回值："Confirmed"---表示指令是Y或 Yes 或 YES 或 yes
           "Not Confirmed"---表示指令是N 或 No 或 NO 或 no
    '''
    if inCMD=='Y' or inCMD=='Yes' or inCMD=='yes' or inCMD=='YES':
        return 'Confirmed'
    elif inCMD=='N' or inCMD=='NO' or inCMD=='No' or inCMD=='no':
        return 'Not Confirmed'
    else:
        return "输入错误"
       #占位语句，添加代码后删除pass

    

if __name__ == '__main__':
    #step1: 输入指令
    inCmd = input("Confirm？(Y[es] or N[o])")
    #step2: 判断输入指令结果
    result = assignment44(inCmd)
    print(result)