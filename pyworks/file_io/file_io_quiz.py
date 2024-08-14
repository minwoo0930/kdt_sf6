# #실습 1
#
# f = open("c:/pyfile/gugudan.txt", "w")
#
# for i in range(1,10):
#     for j in range(1,10):
#         f.write(f'{i} * {j} = {i * j}\n')
#     f.write("\n")
# f.close()
#
#
# f = open("c:/pyfile/gugudan.txt", "r")
# print(f.read())
# f.close()



# 실습2
try:
    with open("./source/member.txt", 'w') as f:
        for i in range(0,3):
            text1 = input("이름 : ")
            text2 = input("비밀번호 : ")
            f.write(text1)
            f.write(" ")
            f.write(text2)
            f.write('\n')


    with open("./source/member.txt","r") as f2:
        data = f2.read()
        print(data)
except FileNotFoundError:
    print("파일을 찾을 수 없습니다")



# 실습 3
