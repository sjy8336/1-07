"""  
파일 입출력(io) 절차
[1] 파일 열기 : 지정된 파일과 노드 연결 => open()
[2] 파일 읽기 / 쓰기 / 수정 => read()/write()
[3] 파일 닫기 : 파일을 모두 사용하고 나면 시스템에서 사용할 수 있도록 반드시 파일 닫기를 해야 한다 => close()
"""

f = open('msg.txt', 'w', encoding = 'utf8')    # w : write 모드. 파일 쓰기
f.write('How are you?')     # W+ : 쓰기 모드로 열어 읽기까지 가능
f.write('반가워요 잘 지냈나요?')
f.close()   # 파일 자원 반납
# 메모리 버퍼에 모아두었던 데이터를 디스크로 보내고 메모리를 비워준다
print('msg.txt에 쓰기 완료!!')
print('-'*50)

# with open() 함수 이용하면 파일 자원 반납을 자동으로 해준다
# close() 호출 안해도 된다

"""  
[실습]
input()으로 입력받은 메시지를
result.txt에 쓰기 모드로 쓰세요(write() 함수 활용)
with open()함수 이용해서 쓰세요
"""
# 내가 함
""" 
with open('result.txt', 'w', encoding = 'utf8') as f:
    f.write(input('메시지를 입력해주세요 >>'))
print('result.txt에 쓰기 완료!') 
"""

message = input('파일에 저장할 메시지 입력>>')
fname = 'result.txt'
# 파일 쓰기 시 기존 내용에 덧붙이고 싶다면: a => append모드
with open(fname, 'a', encoding = 'utf-8') as f:
    f.write('\n' + message)
print(fname, '파일에 쓰기 완료')

# 읽기 모드로 파일 읽을 때
# readlines() ==> list를 반환
# writelines() ==> list를 쓴다
lst = ["Hi\n", "Python\n", "Hello", "Java~"]
# result2.txt에 lst를 쓰세요
with open('result2.txt', 'a') as f:
    f.writelines(lst)
print('result2.txt 쓰기 완료!!')

#파일 입출력
'''
[1] open(파일명, 파일모드, 인코딩)  : 파일 노드를 연결하고 연다.
[2] read() : 해당 파일의 모든 내용을 읽어들여 하나의 문자열로 반환
    readline() : 한 줄 단위로 읽어서 반환. 읽어온 자료는 문자열(str) 자료형으로 반환됨. 반복문 필요함
    readlines() :전체 텍스트 자료를 줄 단위로 읽어온다. 읽어온 자료는 리스트(list) 자료형으로 반환된다.
[3] close() : 파일과 연결된 자원 반납

#파일모드
[1] r : read mode (기본값) 읽기 전용 모드
[2] w : write mode : 쓰기 전용모드
[3] a : append mode 파일 마지막에 새로운 데이터를 추가하는 모드
[4] t : text mode 파일 데이터를 텍스트 파일로 인식하고 입출력함 (기본값)
[5] b : binary mode : 바이너리 파일로 인식하고 입출력함
[6] x : : 쓰기용 파일을 새로 만들어서 연다.(기존 파일이 있으면 error)

# encoding : 인코딩 또는 디코딩에 사용되는 인코딩의 이름을 지정하는 속성으로 텍스트 모드에서만
    사용한다. 기본 인코딩은 플랫폼에 따라 다르지만 파이썬에서 지원하는 인코딩 목록은
    codec 모듈을 참조한다.
'''