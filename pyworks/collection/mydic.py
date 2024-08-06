# 컴퓨터 용어 사전
dic = {
    "비트" : "0이나 1의 값을 가지는 컴퓨터 데이터의 최소 단위",
    "변수" : "어떤 1개의 자료를 저장하기 위한 메모리 할당 공간",
    "리스트" : "여러 개의 연속적인 자료를 저장하는 자료구조"
}

try:
    #에러가 날 수 있는 곳(실행문)에 위에 위치
    print("★ 컴퓨터 사전 ★")
    word = input("검색할 단어를 입력하세요: ")
    print(f'{word}:{dic[word]}')
except KeyError:
    # 에러 처리 메시지
    print("정의된 단어가 없습니다.")

