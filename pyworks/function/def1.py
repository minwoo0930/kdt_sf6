#print("Hello ~ ")
# 인사하는 함수 - greet
# 재사용이 가능한 코드 블럭(조각)

def greet():
    print("안녕~") # 지역 영역


def greeting(name):
    print("안녕~", name)

def get_gugu(dan):
    for i in range(1, 10):
        print(f'{dan} x {i} = {dan * i}')


def add(x,y):
    total = x + y
    print("더하기:", total)

    

add(10,11)
# 메인 영역(실행 영역)


greet() #함수 호출
greeting("다빈") #name = "현수"
greeting("다빈")



get_gugu(4)
