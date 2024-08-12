# time 모듈
# time.time() - 1970.1.1 자정이후부터 시간을 초로 반환

import time
import math

# print(time.time())
# # 일로 환산
# day = time.time() / (24 * 60 * 60)
# print(day)
# # 년으로 환산
# year = math.floor(time.time()/ (365 * 24 * 60 * 60))
# print(year)
#
# # time.sleep(1) - 1초 간격으로 대기
# for i in range(10):
#     print(i)
#     time.sleep(0.5)

# 수행(실행) 시간 측정
strat = time.time()
# print(strat)

for i in range(1000000):
    print(i)
    #time.sleep(1)

end = time.time()
print("수행시간 : " + str(end - strat) + "초")