# -*- UTF-8 -*-
"""
题目：有一列表，存放有若干同学的姓名，编写程序将这些信息分成两组，元素顺序为偶数的
放在一组，奇数的放在另一组，然后将分组的信息进行输出。例如：
["张三","李四", "王五", "赵六", "孙七"," 周八", "吴九"]
分组     1    2     3    4    5
奇数组  张三  王五   孙七 吴九
偶数组  李四  赵六  周八
"""

def  assignment62(lstName):
    '''
    function: 根据序号对名字列表分组
    para: lstName---名字列表
    reval: 分组构成的列表，[[奇数组名字列表],[偶数组名字列表]]
    '''
    #step1: 遍历lstName
    #step1.1: 保存序号为奇数的名字
    ji=[]
    ou=[]
    #step1.2: 保存序号为偶数的名字
    for i in range(1,len(lstName)+1):
        if i%2==1:
            ji.append(lstName[i-1])
        elif i%2==0:
            ou.append(lstName[i-1])
    return [ji,ou]
        
    pass  # 占位语句，完成函数后删除

if __name__ == "__main__":
    #step1 构建名字列表，例如：lstName=["张三","王五","孙七","吴九"]
    lstName=["张三","李四", "王五", "赵六", "孙七"," 周八", "吴九"]
    print(lstName)
    #step2 分组，分成两个list 
    ji=assignment62(lstName)[0]
    ou=assignment62(lstName)[1]
    #step3 输出奇数组的名字信息，每个名字占8列，右对齐
    print (ji,end='\t')
    print (ou,end='\t')
    #step4 输出偶数组的名字信息，每个名字占8列，右对齐

