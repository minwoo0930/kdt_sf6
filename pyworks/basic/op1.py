# 연산자(operator)
# 산술 연산 +, -, *, /, //(나누기의 몫), %(나누기의 나머지)
# 입력

n1 = 10
n2 = 4

# 산술 연산
sum = n1 + n2
sub = n1 - n2
mul = n1 * n2
div = n1 / n2 

#출력
#print(n1, n2)
print(sum) #14
print(sub) #6
print(mul) #40
print(div) #2.5
print(n1 // n2) #2
print(n1 % n2) #2

print(n1 ** n2) #10000
print(2**3)


# 실습
n3 = 30
n4 = 4

몫 = n3 // n4
나머지 = n1 % n2

print(f'빵의 갯수 : {몫}')
print(f'남은 빵의 갯수 : {나머지}')

#실습 해답 - 빵 30, 사람 - 4
bread = 30
people = 4

몫 = bread // people
나머지 = bread % people

print("빵의 개수: str(몫)")
print("남은 빵의 개수: str(나머지)")

