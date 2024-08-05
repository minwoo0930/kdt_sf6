# 자리배치도
# 고객수 - customer, 좌석열 - column, 행 - row
# 나머지가 0일 때 행의 수, 나머지가 0이 아닐 때 행의 수

customer = int(input("고객 수 입력:"))
column = int(input("좌석 열 수 입력:"))


if customer % column == 0 :
    row = customer// column
else:
    row = customer // column + 1

for i in range(0, row):
    for j in range(1, column + 1):
        num = column * i + j
        if num > customer:
            break
        print(num, end = ' ')
    print()




