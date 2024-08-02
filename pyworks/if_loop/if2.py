#다중 조건문
"""
if 조건1:
	실행할 코드(조건1 참일 때)
elif 조건2:
	실행할 코드(조건2 참일 때)
else
	실행할 코드
"""

age = 33
if age < 20:
    print("미성년자 입니다.")
elif age < 30:
    print("20대 입니다.")
elif age < 40:
    print("30대 입니다.")
else:
    print("이제는 중년 ,,,")
print(f'나이는 {age}세입니다.')