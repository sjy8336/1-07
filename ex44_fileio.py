# 파일 입출력 시 예외가 발생함
# 읽거나 쓰고자 하는 파일이 존재하지 않을 경우 => FileNotFoundError
# 인코딩/디코딩이 맞지 않는 경우 => UnicodeDecodeError

def read_file(filename):
    try:
        with open(filename, 'r', encoding = 'utf-8') as f:    # r : read 모드 | W : write 모드
            lines = f.readlines()   # 파일 내용을 list에 담아서 반환함
            # print(lines)    # list에 파일 내용이 담겨서 출력된다
            # print(type(lines))
            for line in lines:
                print(line, end = '')    # line 안에는 '\n' 이 포함되어 있다
    except FileNotFoundError as e:
        print(filename, '파일은 존재하지 않습니다')
    except UnicodeDecodeError as e:
        print('유니코드 디코드 에러! 캐릭셋 설정하세요:', e)
# D:/dev_source/PyWork/out.txt
fname = input('읽을 파일명을 입력하세요>>')
read_file(fname)
"""  
read_file()함수에서 발생 가능성이 있는 예외를 적절하게 처리하세요
D:/dev_source/PyWork/ex44_fileio.py
D:/dev_source/PyWork/ex43_except.py
"""