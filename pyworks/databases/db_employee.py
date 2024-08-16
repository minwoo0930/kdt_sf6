# 사원 관리 - 조회(전체, 1건)
import sqlite3

def select_emp():
    conn = sqlite3.connect('c:/pydb/mydb.db') #db에 연결 - conn 객체 생성
    cur = conn.cursor() #작업 객체 생성
    sql = "SELECT * FROM employee"
    cur. execute(sql)
    rs = cur.fetchall() #db에 있는 자료 모두 가져옴(rs - resultSet)
    print(rs)


    for i in rs:
        print(i)
    conn.close()



#
# def insert_emp():
#     conn = sqlite3.connect('c:/pydb/mydb.db')
#     cur = conn.cursor()
#     sql = "INSERT INTO employee VALUES ('e106', '조대리', 4500000)"
#     cur.execute(sql)
#     conn.commit() #자료 삽입, 수정, 삭제후에는 반드시 commit()
#     conn.close()
# insert_emp()


# 자료 수정
# def update_emp():
#     conn = sqlite3.connect('c:/pydb/mydb.db')
#     cur = conn.cursor()
#     #고신입의 급여를 2500000으로 수정
#     sql = "UPDATE employee SET salary = 2500000 WHERE emp_id = 'e104'"
#     cur.execute(sql)
#     conn.commit()
#     conn.close()
#
# # 함수 호출
# update_emp()
#
# def delete_emp():
#     conn = sqlite3.connect('c:/pydb/mydb.db')
#     cur = conn.cursor()
#     sql = "Delete from employee where emp_id = 'e102'"
#     cur.execute(sql)
#     conn.commit()
#     conn.close()
#
# delete_emp()

def select_one():
    conn = sqlite3.connect('c:/pydb/mydb.db')
    cur = conn.cursor()
    # 이름에 신입이 포함된 사원의 정보를 검색하시오
    sql = "SELECT * FROM employee where name like '%신입%'"
    cur.execute(sql)
    rs = cur.fetchone()
    print(rs)
    conn.close()



select_one()
select_emp()







