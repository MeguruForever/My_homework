import time
day=time.time()//86400
hour=(time.time()%86400)//3600
print ("过去了",format(day,'.0f'),"天",format(hour,'.0f'),"小时")