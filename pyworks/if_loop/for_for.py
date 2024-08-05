
"""
for i in range(1, 5):
    for j in range(1, 5):
        print("가", end = ' ')
    print() #행바꿈

    i =1 
        j = 1,      가 
        j = 2,      가가 
        j = 3,      가가가
        j = 4,      가가가가 
    

for i in range(1, 5): # i = 1, 2, 3, 4
    for j in range(1, i + 1): # j = 1, 2, 3, 4
        print("*", end = ' ')
    print() #행바꿈


for i in range(1, 5):
    for j in range(1, 6 - i) :
        print("*", end = '')
    print()
"""

# 파이썬의 단일 for
for i in range(1, 5):
    print(" " * (4 - i) + "*" * i)


# 숫자가 연속으로 증가하는 알고리즘
for i in range(0, 4):
    for j in range(1, 5):
        num = i * 4 + j
        if num > 15:
            break
        print(num, end=' ')
    print()






