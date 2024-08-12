class Employee:
    serial_num = 1000
    def __init__(self, name):
        self.name = name
        Employee.serial_num += 1 #시리얼 번호를 1 증가
        self.id = Employee.serial_num # 시리얼 번호를 사원 번호에 저장함

# __str__(): 객체 정보를 출력하는 메서드
    def __str__(self):
        return "사번: {0}, 이름 : {1}".format(self.name, self.id)

emp1 = Employee("최사원")
print(emp1)

emp2 = Employee("정사원")
print(emp2)

emp2 = Employee("최사원")
print(emp2)

