"""
변수 선언(변수명 문법)
- 숫자로 시작하면 안됨
- 공백문자가 있으면 안됨
- 특수문자 불가('_' 언더바 가능)

"""

#season2 = "여름"
#season = summer
#2season = "여름"
#season 2 = "summer"
#ag-e = 13

#print(season2)
#print(ag_e)

# 연습
name = 'Harin'
name = 'Jerry'
print(name)

print('*** 회원가입 ***')
user_id = 'kdt6'
user_pw = 'sf1234'
email = "jerry@korea.com"
age = 35

#print("아이디 :", user_id)
print(f'아이디 : {user_id}')
print("비밀번호 :", user_pw)
print("이메일 :", email)
print("나이 :", age)

#소수점 처리하기
# int = 정수, float = 실수

n1 = 10
n2 = 3
div = n1 / n2
print(type(n1))
print(type(div))
print(f'결과값:{div : .2f}')
print(f'결과값: {round(div, 2)}')

#반올림 함수 - round(숫자, 자리수)
print(round(1.647, 2))





