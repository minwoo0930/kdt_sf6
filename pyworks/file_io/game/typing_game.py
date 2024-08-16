import random
import time

with open("words.txt","r") as f:
    word = f.read().split()
text = random.choice(word)
print(text)

n = 1 #문제 번호(1~10)
input("[타자 게임] 준비되면 엔터!")
start = time.time() # 게임 시작 시간
while n < 11:
    print("문제", n)
    question = random.choice(word)
    print(question) #단어 출제
    user = input() #유저가 단어 입력
    if user == question:
         print("통과!!")
         n += 1

    else:
        print("오타!, 다시 도전!!")
end = time.time()
et = end - start
print(f'타자시간: {et : .2f}초')
print("프로그램 종료")





