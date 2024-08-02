# 실습 1

# 조건 - 시내에서 자동차의 주행 속도가 50km 이상이면 "속도 위반입니다."
# 아니면 규정 속도 준수!!

velocity = float(input("속도: "))
if velocity >= 50 :
    print("속도 위반입니다.")
else:
    print("규정 속도 준수!!")
print(f'주행 속도는 {velocity}km입니다.')

