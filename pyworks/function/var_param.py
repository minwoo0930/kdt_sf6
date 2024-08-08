# 가변 매개 변수
# 매개변수의 입력값이 정해지지 않은 변수
# 변수 이름앞에 '*'를 붙인다

def calc_avg(*numbers):
    sum_v = 0
    for i in numbers:
        sum_v += i
        return sum_v/ len(numbers)



avg1 = calc_avg(1, 2, 3)

print(avg1)

avg2 = calc_avg(1, 2, 3, 4)

print(avg2)




