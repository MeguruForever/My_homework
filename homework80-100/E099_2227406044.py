# IPv4 采用 32 位 2 进制位数记录地址，在实际使用中 IPv4 地址通常使用点分十进制记
# 法表示，即使用.将 IP 地址平分为 4 段，每段地址使用 0~255 范围内的十进制无符号整
# 数表示，例如 192.168.1.1。另外 IPv4 地址根据第一段 IP 的值分为 5 类地址，如下表所
# 示，例如 192.168.1.1 是一个 C 类地址。编写一个程序，从键盘输入一个字符串形式的
# IP 地址，判断 IP 地址是否是合法的 IPv4 地址，如果是合法地址，判断其地址类型。
# IP地址分类方法参考：https://baijiahao.baidu.com/s?id=1739492476134586217&wfr=spider&for=pc 
def judge_ip(ip):
    """
    function：判断是否为ip地址，若是，是几类地址
    param:
        ip:输入的ip地址
        result：若为ip地址，直接赋值为几类地址，若为非法地址，赋值为None
    return:result
    example1:
        ip: "192.168.1.1"
        result: "c"
    example2:  如果不是合法的ipv4地址，返回None
        ip: "999.999.999.999"
        result: None
    """
    result=None
    lst=ip.split('.')
    for i in lst:
        if i.isdigit()==False:
            result=None
            break
        else:
            if int(i)>255 or int(i)<0:
                result=None
                break
    else:
        if int(lst[0])>=1 and int(lst[0])<=127:
                    result='a'
        elif int(lst[0])>=128 and int(lst[0])<=191:
                    result='b'
        elif int(lst[0])>=192 and int(lst[0])<=223:
                    result='c'
        elif int(lst[0])>=224 and int(lst[0])<=239:
                    result='d'
        elif int(lst[0])>=240 and int(lst[0])<=255:
                    result='e'
    return result


if __name__ == '__main__':
    ip="192.168.1.1"
    result=judge_ip(ip)
    print(result)