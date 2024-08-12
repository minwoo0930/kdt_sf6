# 정보 은닉(보안을 유지하기 위해 접근을 허용하지 않음)
# 접근 제어자 - public(기본), private, protected
# 외부로 쓰지 않고 내부적으로 작동함

class Person:
    def __init__(self):
        self.__name = ""
        self.age = 0
    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


p1 = Person()
# p1.name = "jerry"
# #p1 = person("jerry")
# print(p1.name)
#set, get 호출

p1.set_name("jerry")
print(p1.get_name)

