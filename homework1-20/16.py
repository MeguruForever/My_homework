time1=list(map(int,input("输入一个时间点用冒号隔开:").split(":")))
time2=list(map(int,input("再输入一个时间点用冒号隔开:").split(":")))
h1=time1[0]
m1=time1[1]
s1=time1[2]
h2=time2[0]
m2=time2[1]
s2=time2[2]
t1=h1*3600+m1*60+s1
t2=h2*3600+m2*60+s2
print (abs(t1-t2))