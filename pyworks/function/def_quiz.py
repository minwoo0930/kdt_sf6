# 실습1
"""
def mul_add(a, b):
    if a == b:

        print(f'결과(곱): {a * b}')
    else :
        print(f'결과(합): {a + b}')


mul_add(2,2)
mul_add(2, 3)
"""
#실습 2
'''
def get_price(x, y):
    price = x * y
    if price < 20000:
        price += 2500
        return price
    else:
        return price

x = int(input("상품 가격:"))
y = int(input("상품 개수:"))
print(f'상품1 가격: {format(get_price(x, y),',d')}')
print(f'상품2 가격: {get_price(5000, 3)}')

'''
#실습 4

"""
def times(a):
    count = 0
    for i in range(1, 31):
        if a * i <= 30: # if i % x == 0:
            count += 1
            print(a * i, end =' ')

    print(f'\n{a}의 배수의 개수: {count}')

times(6)

"""

# 실습 3
def check_machine(a):
    print("남은 음료수는",a)
def is_drink(a):
    if a in vending_machine:
        vending_machine.remove(a)
        print(a, "드릴게요")
    else:
        print(f"{a}는 지금 없네요")
def add_drink(a):
    vending_machine.append(a)
    vending_machine.sort()
    print("추가 완료")

def remove_drink(a):
    if a in vending_machine:
        vending_machine.remove(a)
        print("삭제 완료")


vending_machine = ['게토레이','게토레이','레쓰비', '레쓰비', '생수','생수','생수', '이프로']

while True:
    who = input("사용자 종류를 입력하세요: \n1.소비자 \n2.주인\n")
    if who == '1':
        print("================RESTART")
        drink = input("마시고 싶은 음료?")
        is_drink(drink)
        check_machine(vending_machine)
    elif who == '2':
        todo = input("할 일 선택: \n1.추가 \n2.삭제 \n")
        if todo == '1':
            check_machine(vending_machine)
            drink = input("추가할 음료수?")
            add_drink(drink)
            check_machine(vending_machine)
        elif todo == '2':
            check_machine(vending_machine)
            drink = input("삭제할 음료수?")
            remove_drink(drink)
            check_machine(vending_machine)
        else:
            print("없음")
    else:
        print("없음")


"""
# 실습 3 해답
vending_machine = ['게토레이', '레쓰비', '생수','게토레이', '이프로', '생수']

def check_machine(): # 남은 음료수를 출력하는 함수
    print("남은 음료수: ", vending_machine)

def is_drink():  # 음료수가 있는지 확인하는 함수
    if drink in vending_machine:
       return True
def add_drink():  # 음료수를 추가하는 함수
    vending_machine.append(drink)  # 입력된 drink 추가

def remove_drink():  # 음료수를 제거하는 함수
    vending_machine.remove(drink)

while True:
    who = input("사용자 종류를 입력하세요:\n1.소비자\n2.주인\n")
    if who == '1':
        drink = input("마시고 싶은 음료? ")
        if is_drink():
            print(drink, "드릴게요")
            remove_drink()
            check_machine()
        else:
            print(f"{drink}는 지금 없네요")
    elif who == '2':
        todo = input("할 일 선택(1.추가, 2.삭제) : ")
        print(todo)
        if todo == '1':
            check_machine()
            drink = input("추가할 음료수? ")
            add_drink()
            vending_machine.sort()  # 오름차순 정렬되면서 같은 값끼리 연결됨
            print("추가 완료")
            check_machine()
        elif todo == '2':
            check_machine()
            drink = input("삭제할 음료수? ")
            if is_drink():
                remove_drink()
                print("삭제 완료")
                check_machine()
            else:
                print("음료 없음")
"""