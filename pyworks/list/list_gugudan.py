# 구구단 프로그램 구현 - 리스트

dan = 2
gugu = [] # 구구단의 결과값 저장

for i in range(1, 10):
    gugu.append(dan * i)
    print(f'{dan} x {i} = {gugu[i-1]}')

#print(gugu)
print("========================")

#변수에 출력된 구구단
'''
for i in range(1,10):
    print(f'{dan} x {i} = {dan * i}')
'''

# 구구단 전체 출력
gugudan = []

for i in range(2, 10):
    row = []
    for j in range(1, 10):
        row.append(i * j)
        print(f'{i} x {j} = {row[j-1]}')
    #print(row)
    print()