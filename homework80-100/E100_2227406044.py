# 编写一个程序，实现类似 urlparse 功能，对一个合法的 URL 地址进行解析，解析后的
# 每一部分存放到列表中，并按照一定格式进行输出。
# 例如 URL 为 http://192.168.1.1:8080/index.html?a=1，解析输出的结果如下：
# 协议： http
# 主机域名或 IP： 192.168.1.1
# 端口： 8080
# 路径： index.html
# 参数： a=1

def parseURL(url):
    '''
    function：对URL地址进行解析
    param:
        url:待解析的url地址
        result:解析的结果，存放在字典中
    return：result
    example：
        url: "http://192.168.1.1:8080/index.html?a=1"
        result: {"protocol":"http", "ip" : "192.168.1.1" ,"port": "8080",“path”:"index.html", "args": “a=1” }
        返回的结果必须为字典，字典的key必须均为字符串，且必须按照格式获取
    '''
    result = {}
    indexprotocol = url.find("://")
    result["protocol"] = url[0:indexprotocol]
    indexip=url.find(":",indexprotocol+3)
    result["ip"] = url[indexprotocol+3:indexip]
    indexport=url.find("/",indexip+1)
    result["port"] = url[indexip+1:indexport]
    indexpath=url.find("?",indexport+1)
    result["path"] = url[indexport+1:indexpath]
    result["args"] = url[indexpath+1:]
    return result


if __name__ == '__main__':
    url='http://192.168.1.1:8080/index.html?a=1'
    result=parseURL(url)
    print("协议",result["protocol"])
    print("主机域名或 IP",result["ip"])
    print("端口",result["port"])
    print("路径",result["path"])
    print("参数",result["args"])