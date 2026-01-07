# D:\dev_source\testPkg ==> 프로젝트 외부에 있는 패키지를 가져와보자
import sys
sys.path.append('D:/dev_source/')
import testPkg.myclock as mc

print(mc.getToday())
# ModuleNotFoundError: No module named 'testPkg'
# 외부 패키지 경로를 시스템의 고급 설정 환경변수 path추가해야 함

"""  
import sys
sys.path.append('D:/dev_source/')
외부에 있는 패키지의 상위 디렉토리를 sys모듈 path 에 추가한 후
import하면 해당 패키지 사용 가능하다
"""