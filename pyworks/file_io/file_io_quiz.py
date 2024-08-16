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
# 로그인

name = input ('이름을 입력: ')
pw = input('비밀번호 입력: ')
user = name + " " +pw + "\n"


with open("./source/member.txt", "r") as f:
    member_list = f.readlines()
    # print(member_list)
    # 상태 변수 - True/False

    for member in member_list: #리스트를 순회하면서
        if member == user: #파일에 있는 member의 name, pw와 입력한 user의 name, pw가 일치하면
            sw = True #상태를 True로 저장

    if sw == True:
        print("로그인 성공!")
    else:
        print("로그인 실패!")












