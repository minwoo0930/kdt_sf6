#실습 5
"""
#sum()
print(sum([1,2,3]))
print(max([1,2,3,]))
"""

input_num = input("숫자 여러개 입력 > ").split(" ")
numbers = []
for i in input_num:
    numbers.append(int(i))
print(numbers)

print(f'가장 큰 값:  {max(numbers)}')
print(f'가장 작은 값:  {min(numbers)}')

numbers.remove(max(numbers))
numbers.remove(min(numbers))

numbers_avg = sum(numbers)/len(numbers)
print(f'나머지 값의 평균:  {numbers_avg}')

