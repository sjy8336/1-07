"""  
예외 처리 방법
try:
    예외 발생 가능 코드
except 예외명 as 변수명:
    예외 처리 코드
else:
    try절 예외가 발생하지 않을 경우 실행할 코드
finally:
    반드시 실행해야 하는 코드
------------------------------------
- 이 때 except 블럭은 여러 개 올 수 있다
- try나 finally는 한 번만 가능
"""

print('---프로그램 시작-------------')
lst = [1,2,3]
try:
    for i in range(5):
        print(lst[i])
    print('>>> 반드시 실행되어야 할 코드')
except IndexError as ex:
    print('에러랍니다?')

print('---프로그램 끝-------------')

# 테스트 해보고 발생된 예외를 적절히 처리하세요
# try ~ except ~ finally 블럭 이용할 것
