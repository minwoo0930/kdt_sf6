# 영어 단어장 만들기

# 경로 - game 폴더에 위치함, 단어장 파일 - words.txt
import random

with open("words.txt", 'w') as f:
    word = ['sky', 'earth', 'moon', 'flower', 'tree', 'apple',
                'mountain', 'garlic', 'onion', 'potato']
    for i in word:
        f.write(i + " ")


with open("words.txt","r") as f:
    #print(f.read())
    data = f.read().split()
    print(data)
    random.choice(data)
    print(random.choice(data))


