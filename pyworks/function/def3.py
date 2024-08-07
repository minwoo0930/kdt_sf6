# 1부터 n까지 곱하는 함수

def gob_n(n):
    gob_v = 1
    for i in range(1, n+1):
        gob_v *= i
    return gob_v

print(gob_n(10))



def du_v(n):
    du_v = 0
    for i in range(1, n + 1):
        du_v += i
    return du_v
print(du_v(4))