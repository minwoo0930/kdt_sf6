# global - 전역변수임을 알려주는 키워드

def one_up():
    global x
    x += 1
    return x

x = 0 #전역변수
print(one_up()) #1
print(one_up()) #2
print(one_up()) #3
print("x =", x)





