# 다중 if 실습
# 점수가 마이너스일 경우 "올바른 점수를 입력해주세요"
score = int(input("점수 입력:"))
grade = "" #빈 문자열
'''
if score >0:
    if score >= 90 and score <= 100:
        grade = "A"
    elif score < 90 and score >= 80:
        grade = "B"
    elif score < 80 and score >= 70:
        grade = "C"
    elif score < 70 and score >= 60:
        grade = "D"
    else:
        grade = "E"
    print(f'{grade} 등급입니다.')
else:
    print("올바른 점수를 입력해주세요.")
'''
if score < 0 :
    print("올바른 점수를 입력해주세요.")
