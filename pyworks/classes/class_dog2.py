class Dog:
    tricks = []#클래스 변수(요소가 누적되고, 초기화가 안됨)
    def __init__(self, name):
        self.name = name
        self.tricks = []
        print("생성자 매서드입니다.")
    def add_trick(self, trick):
        self.tricks.append(trick)


dog1 = Dog('John')
dog1.add_trick("몸 뒤집기")
print(dog1.tricks)

dog2 = Dog('Jerry')
dog2.add_trick("죽은척 하기")
print(Dog.tricks) # 클래스 이름으로 접근하기