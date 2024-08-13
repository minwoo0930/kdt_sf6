# try ~ except ~ finally

def divide(x, y):
    try:
        result = x/y
        print(result)
    except ZeroDivisionError:
        print("0으로 나눌 수 없음")

    finally:
        # 실행이 성공하든 실패하던 반드시 실행되어야 함
        # 예 (마이크로 프로세서에서 재부팅하는 경우)
        
        print("여기는 반드시 수행됩니다.")

divide(2, 3)

