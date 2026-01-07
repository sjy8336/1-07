# 내장 표준 모듈 리스트 확인
import sys
# print(sys.builtin_module_names)
print('#'*50)
import math
print(math.pi)
print(math.pow(2, 6))
# 5! = 1X2X3X4X5 = 120
print(math.factorial(5))
print(dir(math))
print('------------------------------------------')

import datetime
print(datetime.datetime.now())  # 현재 날짜와 시간 출력
# 2026-01-07 10:00:02.352373
print(datetime.date.today())    # 날짜만 출력   2026-01-07

tday = datetime.date.today()
yy = tday.year
mm = tday.month
dd = tday.day
print(yy, '년')
print(mm, '월')
print(dd, '일')
# 날짜와 시간 변경
# datetime의 replace() 메소드 사용
s_time = datetime.datetime.now()
print(f's_time: {s_time}')
# s_time: 2026-01-07 10:04:57.431478

s_time = s_time.replace(month = 4, day = 5)
print('날짜 변경 후 ---------------------------------')
print(f's_time: {s_time}')  #s_time: 2026-04-05 10:06:35.841858

# datetime.datetime.now()
# datetime 모듈에 별칭을 주어 참조해보자
# import 모듈명 as 별칭
import datetime as dt
s_time : dt.datetime.now()
print(f's_time: {s_time}') 
# 요일 정보
print(s_time.weekday())
days = ['월', '화', '수', '목', '금', '토', '일']
print(days[s_time.weekday()], '요일')

# 2026년 8월 15일이 무슨 요일인지 알아내서 출력해보세요
theDay = dt.datetime.now()
theDay = theDay.replace(month = 8, day = 15)
print(f'광복절: {theDay}')
print(days[theDay.weekday()])

d_day = dt.datetime(2026, 11, 17, hour = 8, minute = 10)
print(d_day)
today = dt.datetime.now()
print(today)
# http://docs.python.org

time_gap = d_day - today
# 수능일까지 남은 시간
print(f'time_gap: {time_gap} type: {type(time_gap)}')
print(time_gap.days, '일 남았습니다')

# [1] 오늘 날짜와 함께 올해 크리스마스까지 남은 날짜와 시간을 구해 출력해보세요
#     올해 크리스마스까지 xx일 xx시간 남았습니다
""" Christmas = dt.datetime(2026, 12, 25)
toDay = dt.datetime.now()
Dday = Christmas - toDay
print = (Dday)
print(f'올해 크리스마스까지 {Dday} 일 남았습니다') """
x_mas = dt.datetime(2026, 12, 25)
tday = dt.datetime.now()
gap = x_mas - tday
print(f'오늘 날짜: {tday.year}/{tday.month}/{tday.day} {days[tday.weekday()]}')
print(f'크리스마스 날짜: {x_mas.year}/{x_mas.month}/{x_mas.day} {days[x_mas.weekday()]}')
hour = 60*60    # 3600
print('크리스마스까지 {}일 {}시간 남았습니다!!!'.format(gap.days, gap.seconds/hour))

# [2] 다가오는 자신의 생일까지 남은 날짜와 시간을 출력해보세요
birth = dt.datetime(2026, 3, 13)
Gap = birth - tday
print('내 생일까지 {}일 {}시간 남았돠!!!'.format(Gap.days, Gap.seconds/hour))

# 100일 뒤 날짜 구하기
# datetime 모듈의 timedelta 라는 클래스를 이용하면
# + - 연산자 이용하여 시간의 차이 연산 가능

# 100일 뒤 경과 시간 구하기
day100 = dt.timedelta(days = 100)
print(day100)
after100 = dt.datetime.now() +day100    # 100일 뒤: 2026-04-17 10:58:13.778358
print(f'100일 뒤: {after100}')
# 100일 전 날짜도 출력하세요
before100 = dt.datetime.now() - day100
print(f'100일 전: {before100}')

# 현재 시간 3시간 뒤를 출력하세요
""" hour3 = dt.timedelta(hours = 3)
aT = dt.datetime.now() + hour3
print(f'3시간 뒤: {aT}') """

after3 = dt.datetime.now() + dt.timedelta(hours = 3)
print(after3)

# 현재 시간 2시간 전을 출력하세요
""" hour2 = dt.timedelta(hours = 2)
aT2 = dt.datetime.now() - hour2
print(f'2시간 뒤: {aT2}') """

before2 = dt.datetime.now() - dt.timedelta(hours = 2)
print(before2)
# time 모듈
"""  
- 시간 관련 정보를 제공하는 모듈
- 1970년 1월 1일 0:0:0 UTC를 기준으로 지금까지 경과한 시간을
    백만분의 1초 단위로 기록하고 저장하는 체계를 갖는다
    이 시작 시간을 epoch라고 함ㄴ
"""
import time
seconds = time.time()
print(seconds)   # 70/1/1 이후 경과한 시간을 초단위로 표시   1767751591.0281277
unit = 60*60*24*30.44*12
print(unit)
ctime = seconds//unit
print('ctime:', ctime)
print(int(1970+ctime))

# time 모듈의 localtime() 사용하면 연산을 다 해준다
local_time = time.localtime(seconds)
# time 모듈의 strftime()을 이용해서 날짜와 시간 서식포맷을 이용해 출력
print(time.strftime('%Y - %m - %d %H:%M:%S', local_time))
# 2026 - 01 - 07 11:15:04

# time 모듈을 이용하면 시계를 만들 수 있다
# time.sleep(초) : 지정된 초 시간동안 block된다

""" while True:
    print('오늘도 즐거운 하루되세요~~')
    time.sleep(2)   # 2초 동안 블럭
"""

import datetime as dt
print(dt.datetime.now())

# from 모듈명 import 함수명[변수]클래스명
from datetime import datetime
print(datetime.now())