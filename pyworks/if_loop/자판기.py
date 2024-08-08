# 과제1 자판기 프로그램
"""
vending_machine = ['게토레이', '레쓰비', '생수', '이프로']

while True:
    print("================RESTART")
    drink = input("마시고 싶은 음료?")
    if drink in vending_machine:
        vending_machine.remove(drink)
        print(drink, "드릴게요")
        print("남은 음료는", vending_machine)
    else:
        print(f"{drink}는 지금 없네요")
"""


#과제 2 자판기 프로그램
vending_machine = ['게토레이','게토레이','레쓰비', '레쓰비', '생수','생수','생수', '이프로']

while True:
    who = input("사용자 종류를 입력하세요: \n1.소비자 \n2.주인\n")
    if who == '1':
        print("================RESTART")
        drink = input("마시고 싶은 음료?")
        if drink in vending_machine:
            vending_machine.remove(drink)
            print(drink, "드릴게요")
            print("남은 음료는", vending_machine)
        else:
            print(f"{drink}는 지금 없네요")
    elif who == '2':
        todo = input("할 일 선택: \n1.추가 \n2.삭제 \n")
        if todo == '1':
            print("남은 음료는", vending_machine)
            drink = input("추가할 음료수?")
            vending_machine.append(drink)
            vending_machine.sort()
            print("추가 완료")
            print("남은 음료는", vending_machine)
        elif todo == '2':
            print("남은 음료는", vending_machine)
            drink = input("삭제할 음료수?")
            if drink in vending_machine:
                vending_machine.remove(drink)
                print("삭제 완료")
                print("남은 음료는", vending_machine)
            else:
                print("없음")
    else:
        print("없음")

