import datetime
time1=list(map(int,datetime.datetime.now().strftime("%H:%M:%S").split(":")))
h=time1[0]
m=time1[1]
s=time1[2]
print (h+1,":",m+15,":",s)