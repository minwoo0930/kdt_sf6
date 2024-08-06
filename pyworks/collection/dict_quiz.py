# 실습1 딕셔너리 사용

student_score = {"Alice":85, "Bob":90, "Charlie": 95} #딕셔너리 생성
print(student_score)
student_score["David"] = 80 # David 요소 추가
print(student_score)
student_score["Alice"] = 88 # Alice 요소 수정
print(student_score)
student_score.pop("Bob") # Bob 요소 삭제
print(student_score)
for student in student_score: # 요소 전체 출력
    print(student,':', student_score[student])

