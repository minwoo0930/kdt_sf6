
age = int(input("나이를 입력해주세요:"))

pay = input("결제 방법을 입력해주세요.('카드' 또는 '현금'만 입력):")

cost = ""
if pay == "카드" :
    if age < 8 :
        cost = "무료"
    elif age < 14 :
        cost = "450원"
    elif age < 20 :
        cost = "720원"
    elif age < 75 :
        cost = "1200원"
    else :
        cost = "무료"
else :
    if age < 20 :
        cost = "1000원"
    elif age < 75:
        cost = "1300원"
print(f'{age}세의 {pay} 요금은 {cost} 입니다.')


""" 
# Quiz4 해답 
age = int(input("나이를 숫자로 입력해 주세요: "))
payment = input("결제 방법을 입력해주세요(카드 또는 현금만 입력): ")
fee = ""

if age < 8:
    fee = "무료"
elif age < 14:
    fee = "450원"
elif age < 20:
    if payment == "카드":
        fee = "720원"
    else:
        fee = "1000원"
elif age < 75:
    if payment == "카드":
        fee = "1200원"
    else:
        fee = "1300원"
else:
    fee = "무료"
print(f'{age}세의 {payment} 요금은 {fee} 입니다.')

"""