import datetime
import time
a = 0
while 4 > 3:
    time1 = datetime.datetime.now().strftime('%H:%M:%S')
    time2 = datetime.datetime.now().strftime('%H:%M:%S')
    a = a + 1

    if time1 == time2:
        pass
    else:
        print(a,time2)
