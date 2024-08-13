# 실습1
# import random
#
# random1 = []
# for i in range(0,4):
#     random1.append(random.randint(1, 100))
#
# print(random1)
# list.sort(random1)
# print(random1)

import random

random1 = set()
while True:
    a = len(random1)
    if a < 6 :
        n = random.randint(1, 45)
        if n not in random1:
            random1.add(n)
        print(len(random1))

    else:
        break

print(random1)
random1_list = list(random1)
random1_list.sort()
print(random1_list)