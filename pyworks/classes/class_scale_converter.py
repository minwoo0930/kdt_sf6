# 단위 변환기 클래스 만들기
# KB = 1,024B(2의 10제곱), B > KB > MB > GB > TB
# 1inch = 2.54cm = 25.4mm
class ScaleConverter:
    # 생성자 매서드
    def __init__(self, units_from, units_to, factor):
        self.units_from = units_from #단위
        self.units_to = units_to     #변환할 단위
        self.factor = factor         #변환값

    # 단위 변환 매서드
    def convert(self, value):
        return self.factor * value


    # 객체의 정보를 출력하는 매서드
    def __str__(self):
        return f'{self.units_from}, {self.units_to}, {self.factor}'


# con 객체 생성
con = ScaleConverter('MB','KB',1024)
print(con)
# print("1MB를 변환하기")
# print(str(con.convert(1)) + con.units_to)
print(f'2{con.units_from} = {con.convert(2)}{con.units_to}')

con2 = ScaleConverter('inch','mm',25.4)
print(f'1{con2.units_from} = {con2.convert(2)}{con2.units_to}')


