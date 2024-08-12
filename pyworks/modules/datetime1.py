import datetime
# 날짜와 시간 모두 출력
now = datetime.datetime.today()
print(now)

print(now.year) #년
print(now.month)
print(now.day)

# 날짜만 출력
print(f'{now.year}-{now.month}-{now.day}')

# 시간만 출력
print(f'{now.hour}:{now.minute}:{now.second}')

# 2023년 7월 31일 출력
the_day = datetime.date(2023, 7 ,31)
print(the_day)

today = datetime.date.today()
print(today)

print(" 지금까지 몇 일?")
passed_time = today - the_day
# print(passed_time)
print(f'개강 이후 {passed_time.days}일 지났습니다.')

# 추석까지 D-day 사용해서 구현
추석 = datetime.date(2023,9,17)
print(추석)

추석D_Day = 추석 - the_day
print(f'추석까지 {추석D_Day}일 남았습니다.')

