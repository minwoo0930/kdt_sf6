class Calculator:

    def __init__(self):
        self.x = 0

    def add(self, y):
        self.x += +y
        return self.x

    #sub() 매서드 생성
    def sub(self, y):
        self.x -= y
        return self.x

c1 = Calculator()
print(c1.x)
print(c1.add(10)) #10 더하기
print(c1.x)
print(c1.sub(5))
print(c1.x)



