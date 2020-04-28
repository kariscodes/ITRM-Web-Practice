#
# Succeed... using by pymysql
#

import pymysql

# MySQL Connection 연결
# connection = pymysql.connect(host='127.0.0.1',
#                              user='DATABASE_USER',
#                              password='PASSWORD',
#                              db='DATABASE_NAME')

# Google Cloud Platform - Database Instance External IP Addr. : 34.82.158.37
# default port number : 3306
try:
    conn = pymysql.connect(host='34.82.158.37', user='dev1', password='dev2020', db='myasset', charset='utf8')
except Exception as e:
    print('Exception occurred!')
    print(e)

# Proxy connection under Proxy server running in GCP
# default port number : 3307
# try:
#     conn = pymysql.connect(host='127.0.0.1', user='dev1', password='dev2020', db='myasset', charset='utf8')
# except Exception as e:
#     print('Exception occurred!')
#     print(e)
# except pymysql.err as e:
#     print('pymysql Exception occurred!')
#     print(e)

# Connection 으로부터 Cursor 생성
curs = conn.cursor()

# SQL문 실행
sql = "select * from member_table"
curs.execute(sql)

# 데이타 Fetch
rows = curs.fetchall()
print(rows)  # 전체 rows
# print(rows[0])  # 첫번째 row: (1, '김정수', 1, '서울')
# print(rows[1])  # 두번째 row: (2, '강수정', 2, '서울')

# Connection 닫기
conn.close()