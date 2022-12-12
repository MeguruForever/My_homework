# 编写一个函数，将一个 a 进制的数转换成一个 b 进制的数，其中 a 和 b 都在[2, 16]之间。
# 该函数有 3 个参数，前两个参数分别是 a 和 b，第三个参数是一个字符串，表示 a 进制
# 的数。如果 a 和 b 不在给定范围之内，返回 None，否则返回对应的 b 进制数


def transfer(a,b,c):
    '''
    function:根据题目要求完成进制转换
    param:
        a:a进制
        b:b进制
        c:a进制对应的数
        res:b进制对应的数
    return：res
    example:
        2,10,'10'==>'2'
        10,2,'2'==>'10'
        10,17,'9'==>None
        17,2,'8'==>None
        13,10,'a'==>'10'
    '''
    if a not in range(2,17) or b not in range(2,17):
        return None
    if a<10:
        res=0
        for i in range(len(c)):
            res+=int(c[i])*a**(len(c)-i-1)
    elif a>10:
        if c.isdigit():
            res=int(c)
        elif c.islower():
            if c=='a':
                res=10
            elif c=='b':
                res=11
            elif c=='c':
                res=12
            elif c=='d':
                res=13
            elif c=='e':
                res=14
            elif c=='f':
                res=15     
    else:
        res=int(c)
    result=''
    while res!=0:
        if res%b<10:
            result+=str(res%b)
        elif res%b==10:
            result+='a'
        elif res%b==11:
            result+='b'
        elif res%b==12:
            result+='c'
        elif res%b==13:
            result+='d'
        elif res%b==14:
            result+='e'
        elif res%b==15:
            result+='f'
        res=res//b
    return result[::-1]
        
        
            
    

if __name__ == "__main__":
    a,b,c =3,10,'11'
    res = transfer(a,b,c)
    print(res)