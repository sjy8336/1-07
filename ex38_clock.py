"""  
time 모듈 이용하여
현재 시간 - 년월일 시분초를 출력하는
my clock이란 함수를 구성하세요
이 함수를 호출하면 1초 단위로
"년월시 시:분:초"를 가져와 출력합니다
"""

# import time
from time import time, sleep, localtime, strftime
# from time import *

def myclock():
    # 무한루프 돌면서 time 정보 구하고 출력
    # 1초 단위로 갱신
    while True:
        seconds = time()
        # print(seconds)
        ltime = localtime(seconds)
        strtime = strftime('%Y-%m-%d %H:%M:%S')
        print(strtime)
        # time.sleep(1)
        sleep(1)
myclock()

""" 
def myclock():
    today = time()
    local_time = time.localtime(today)
    print(time.strftime('%Y - %m - %d %H:%M:%S', local_time))
    time.sleep(1)
    return myclock()
myclock()
"""