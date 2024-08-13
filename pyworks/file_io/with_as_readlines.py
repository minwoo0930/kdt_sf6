with open ('source/city.txt', 'r') as f:
    # data = f.readlines()
    # data = f.readline().split()
    # print(data)

    a = []
    for i in range(6):
        data = f.readline().split(' ')
        a.append(data)

    print(a)

    #리스트 요소 출력
    print(a[0])
    print(a[-1])
    print(a[0][0])
    print(a[-1][0])

    for i in a:
        print(i)



