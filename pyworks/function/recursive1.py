#재귀함수 - 자기 자신을 호출하는 함수

def sos(n)
    print("Help me!!")
    if n == 1:

        return ""
    else

        return sos(n-1)
    sos(5)

# 팩토리얼 계산
def facto(n):
    if n == 1
        return 1
    else:
        return n * facto(n-1)

print(facto(4))
