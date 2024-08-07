# 실습1
"""
def mul_add(a, b):
    if a == b:

        print(f'결과(곱): {a * b}')
    else :
        print(f'결과(합): {a + b}')


mul_add(2,2)
mul_add(2, 3)
"""
#실습 2
def get_price(x, y):
    price = x * y
    if price < 20000:
        price += 2500
        return price
    else:
        return price

x = int(input("상품 가격:"))
y = int(input("상품 개수:"))
print(f'상품1 가격: {format(get_price(x, y),',d')}')
print(f'상품2 가격: {get_price(5000, 3)}')
