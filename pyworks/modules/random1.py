# random 모듈
import random
import math

# # 랜덤수 출력(0.0 <= r < 1)
# print(random.random())
#
# # 주사위(dice) - 방법 1
# dice = random.randint(1,6)
# print(dice)
#
# # 주사위 - 방법 2
# dice2 = math.floor(random.random() * 6) + 1
# print(dice2)
#
# # 주사위 10번 던지기

for i in range(0,10):
    dice = random.randint(1, 6)
    print(dice)

# 랜덤하게 단어 추출하기

words = ['여름', '꽃', '나비', '벌', '나무']

print(random.choice(words))

# 방법2 - 주의!
idx = math.floor(random.random() * len(words))
print(idx)
print(words[idx])
