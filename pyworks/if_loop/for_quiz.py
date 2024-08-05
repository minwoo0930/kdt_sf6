# 실습 1
"""
total = 0
num = int(input("어디까지 계산할까요?"))
for i in range(num + 1):
    total += i
print(f'1부터 {num}까지의 합: {total}')

"""
# 실습 1 번외
"""
total = 0
num = int(input("어디까지 계산할까요?"))
for i in range(1, num + 1):
    if i% 2 == 0 : 
    total += i
print(f'1부터 {num}까지의 합: {total}')
"""

# 실습 2
"""
n = int(input("몇 초?"))
for i in range(n, 0, -1):
    print(i, end =' ')
print("발사!!")

몇 초?5
5 4 3 2 1 발사!!
"""

# 실습 3
n = int(input("몇 단을 출력할까요?"))

for i in range(1, 10):
    result = i * n
    print(f'{n} * {i}  = {result}')