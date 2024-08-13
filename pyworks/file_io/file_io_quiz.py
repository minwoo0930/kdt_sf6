#실습 1

f = open("c:/pyfile/gugudan.txt", "w")

for i in range(1,10):
    for j in range(1,10):
        f.write(f'{i} * {j} = {i * j}\n')
    f.write("\n")
f.close()


f = open("c:/pyfile/gugudan.txt", "r")
print(f.read())
f.close()
