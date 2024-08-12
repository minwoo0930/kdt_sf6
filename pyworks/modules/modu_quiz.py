# 실습1
import random

random1 = []
for i in range(0,4):
    random1.append(random.randint(1, 100))

print(random1)
list.sort(random1)
print(random1)