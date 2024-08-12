
import sys

class Calculator():

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def sub(self):
        return self.x - self.y

    def mul(self):
        return self.x * self.y

    def div(self):
        if self.y == 0:
            print("0으로 나눌 수 없음")
            return sys.exit(0)
        return self.x / self.y

cal = Calculator(12,0)
print(cal.add())
print(cal.sub())
print(cal.mul())
print(cal.div())


#실습 2 -Supermarket 클래스
"""
class Supermarket():
    def __init__(self, location, name, product, customer):
        self.location = location
        self.name = name
        self.product = product
        self.customer = customer
    def show_info(self):
        print(f'위치:{self.location}, 이름:{self.name}, 상품:{self.product}, 고객수:{self.customer}')
    def print_location(self):
        print(f'위치:{self.location}')

    def change_category(self, product):
        self.product = product

    def show_list(self):
        print(f'상품 : {self.product}')
    def enter_customer(self):
        self.customer += 1

customer1 = Supermarket('마포구 염리동', '마켓온', '과일', 12)

customer1.print_location()
customer1.change_category('음료')
customer1.show_list()
customer1.show_info()


# class SuperMarket:
#     def __init__(self, location, name, product, customer):
#         self.location = location # 위치
#         self.name = name  # 가게 이름
#         self.product = product # 파는 물건
#         self.customer = customer # 고객의 수
#
#     def print_location(self):
#         print(f'위치: {self.location}')
#
#     def change_category(self, another_product):
#         self.product = another_product
#
#     def show_list(self):
#         print(f'상품: {self.product}')
#
#     def enter_customer(self):
#         self.customer += 1  #self.customer = self.customer + 1
#
#     def show_info(self):
#         print(f'위치: {self.location}, 이름: {self.name}, '
#               f'상품: {self.product}, 고객수: {self.customer}')
#
#
# super1 = SuperMarket("마포구 염리동", "마켓온", "과일", 10)
# super1.print_location()
# super1.change_category("음료")
# super1.show_list()
# super1.enter_customer() #고객 1 들어옴
# super1.enter_customer() #고객 1 들어옴
# super1.show_info()

"""







