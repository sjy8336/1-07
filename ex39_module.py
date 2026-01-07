"""  
패키지

- 패키지: mypkg
mypkg폴더
    - myclock.py : 시계 모듈
    - circleArea.py : 원의 면적
    - rectArea.py : 사각형 면적
    - triangleArea.py : 삼각형 면적
- 유사한 기능을 가진 모듈 여러개를 패키지로 묶어 관리할 수 있다.
목적: 관리 용이성 + 배포 용이성
구성방법:
    1) 디렉토리 생성
    2) 해당 디렉토리 내에 _init_.py 파일을 생성
        파이썬3 이상은 _init_.py 파일이 없어도
        자동으로 패키지 인식을 한다
        => 하위 버전과의 호환성을 위해 생성하자

------------------------
# 패키지 사용 시
import 패키지명.모듈명
from 패키지명.모듈명 import 함수...
...
"""

# [1] mypkg 패키지의 mycircle의 getCircleArea()를 추출하여
# 반지름이 10cm인 원의 면적을 구하고
# 아래와 같이 출력하세요    (circle_format()활용)
# "반지름이 10cm인 원의 면적: 314.15"
import mypkg.mycircle as mc
result = mc.getCircleArea(10)
# print(result)
result = round(result,2)
mc.circle_format(result, msg='반지름이 10cm인 원의 면적')

# [2] myrect 모듈 활용
# 가로: 13 세로 27인 사각형의 면적을 구해
# 출력
# "가로: 13cm 세로 27cm인 사각형 면적: xxx"
import mypkg.myrect as mr
result = mr.getRectArea(13, 27)
mr.rect_format(result, '가로: 13cm, 세로: 27cm인 사각형의 면적')

# [3] myclock 모듈 활용
# 오늘 날짜 출력하세요
from mypkg.myclock import getToday, myclock
print(getToday())

myclock()