# 이차원 리스트 - 리스트 내부에 리스트 있음
# matrix - 행, 열로 이루어짐
d = [
    [10, 20],
    [30, 40],
    [50, 60]
]
print(d)
print(type(d))

# 인덱싱 - 요소 접근(조회)
print(d[0][0])
print(d[0][1])

# 인덱싱 - 요소 접근(조회)
print(d[0][0])
print(d[0][1])
print(d[1][0])
print(d[1][1])
print(d[2][0])
print(d[2][1])

# 요소 추가
d.append([70, 80])
print(d)

# 요소 수정
d[0][0] = 90
print(d)
d[0][1] = 100
print(d)

# 요소 삭제
#d[1].pop(1) # 40 삭제
#print(d)

#리스트의 크기
a = [1, 2, 3]
print(len(a))

#전체 조회
print("리스트의 크기(행):",len(d))
print("리스트의 크기(열):", len(d[0]))
print("리스트의 크기(열):", len(d[1]))


for i in range(len(d)) :
    for j in range(len(d[i])) :
        print(d[i][j], end = " ")
    print()

# for in 리스트

for x, y in d:
    print(x, y)