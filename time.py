import datetime
import time

timeStamp = 1522744119916 #毫秒
timeStamp  = timeStamp/1000.0 #先转化为秒
print(timeStamp)
real_time = time.localtime(timeStamp)
other_style_time = time.strftime("%Y-%m-%d %H:%M:%S",real_time)
print(other_style_time)
