import time 
from trafic_condition import get_duration
from wind_condition import get_wind


def get_time():
    timenow=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    return timenow

def gotit():
    while True:
        local_time =time.localtime()
        aim_time = local_time.tm_min
        if aim_time%10 == 0:
                get_duration()
                get_wind()
                time.sleep(60*5)
        
        else:
                #print(time.time())
                time.sleep(60)
gotit()