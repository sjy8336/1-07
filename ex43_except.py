def except_pass_test():
    print('---예외 처리 회피 테스트-------')
    try:
        print(10/5)
        print(int('asdf'))
    except ZeroDivisionError:
        pass
    except Exception as ex:
        print('기타 오류 발생: ', ex)
        return  # 제어 흐름이 함수를 호줄한 쪽으로 이동한다
    finally:
        print('--반드시 실행돼야 할 코드---------')     # return문이 와도 finally블럭은 수행한다
    print('--예외 처리 회피 테스트 끝--------')

def except_detail_test():
    print('---오류 상세 정보 출력 테스트--------')
    try:
        print(10/2)
        print(int('asdf'))
    except Exception as e:
        print(f'오류 종류: {type(e).__name__}')
        print(f'오류 발생 파일명: {__file__}')
        print(f'오류 발생 위치: {e.__traceback__.tb_lineno}번째 라인')
    print('---오류 상세 정보 출력 테스트 끝--------')

print('--프로그램 시작---')
# except_pass_test()
except_detail_test()
print('---프로그램 끝')