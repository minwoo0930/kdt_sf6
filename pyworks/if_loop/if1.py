# if문  - 조건: 나이가 15세 이상이면 "관람가" 출력
# 구문 만들 때 끝에 콜론(:)을 붙이고 다음줄에서 4칸 띄어씀(인덴트)

age = 10

"""
if age >= 15: # 조건이 True일 때 실행 
    print("관람가")
print(f'나이는 {age}세 입니다.')
"""
# if ~ else문 조건이 True이면 if문 실행하고, 조건이 False이며 else문을 실행함
if age >= 15: # 조건이 True일 때 실행
    print("관람가")
else:
    print("관람불가")
print(f'나이는 {age}세 입니다.')

# 어떤 수를 짝수인지 홀수인지 판별하는 프로그램
# 짝수 -> 2의 배수(2, 4, 6 ...) - 2로 나눈 나머지 0 어떤수 % 2 == 0

num = int(input("수를 입력하세요: "))
if num % 2 == 0:
    print("짝수") 
else :
    print("홀수")
print(f'입력된 수는 {num}입니다')

