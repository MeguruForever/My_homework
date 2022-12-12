# 96. 给定字符串，将其中的单词倒序输出。例：给定"What a wonderful day!"，输出： "day!
# wonderful a What"。

def reverse_sentence(input_str):
    """
    function：将给定字符串中的单词进行倒序排序输出
    param:
        input_str:输入的字符串
        result:倒序排序后的字符串
    return:result
    example:
        input_str: "What a wonderful day!"
        result:  "day! wonderful a What"
    """
    result=""
    list=input_str.split(" ")
    for i in range(len(list)-1,-1,-1):
        result+=list[i]+" "
    return result



if __name__ == '__main__':
    input_str="What a wonderful day!"
    result=reverse_sentence(input_str)
    print(result)