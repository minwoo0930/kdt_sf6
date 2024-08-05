# for in 리스트
"""
shop = ['반팔티', '바지', '이어폰', '키보드']

print('바지' in shop)
print('양말' in shop)
print('양말' not in shop)

# '마우스' 추가
shop.append('마우스')
print(shop[:])

# '이어폰' 삭제
shop.remove('이어폰')

# 리스트 요소 추가
shop.extend(['커피', '비스켓'])
print(shop[:])

for i in shop:
    print(i)
"""

# 리스트의 연산
# 개수, 합계, 평균, 최대값, 최소값
score = [70, 80, 60, 90, 40]

print(f'개수: {len(score)}')
print(f'합계: {sum(score)}')
print(f'평균: {sum(score)/len(score)}')
print(f'최대값: {max(score)}')
print(f'최소값: {min(score)}')

# 합계
sum_v = 0
for i in score:
    sum_v += i
print(f'합계: {sum_v}')

#최대값
max_v = score[0] # 처음 값으로 초기화 또는 터무니 없이 작은값으로 설정
n = len(score)
for i in range(0, n):  # n + 1이 아닌 n
    if score[i] > max_v:
        max_v = score[i]
print(f'최대값: {max_v}')

"""
    i=1 80>70, max_v = 80 
    i=2 60>80, max_v = 80(유지) 
    i=3 90>80, max_v = 90 
    i=1 40>90, max_v = 90(유지)
"""
#최소값
min_v = score[0]
n = len(score)
for i in range(0, n):
    if score[i] < min_v:
        min_v = score[i]
print(f'최소값: {min_v}')





