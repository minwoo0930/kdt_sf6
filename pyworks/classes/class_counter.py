#카운터 만들기 - 클래스 변수
class Counter:
    x = 0 #클래스 변수
    def __init__(self):
        Counter.x += 1

c1 = Counter()

print(Counter.x) #1

c2 = Counter()

print(Counter.x) #2

c3 = Counter() #3

print(Counter.x)

class Counter2:
    def __init__(self):
        self.x = 0
        self.x += 1

count1 = Counter2()
print(count1.x)

count2 = Counter2()
print(count2.x)