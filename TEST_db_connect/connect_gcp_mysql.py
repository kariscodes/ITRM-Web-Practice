#
# Failed...
#

import pymysql
import sqlalchemy
# import os

DB_USER = "dev1"
DB_PASS = "dev2020"
DB_NAME = "myasset"
CLOUD_SQL_CONNECTION_NAME = "our-velocity-271006:us-west1:das"

# db_user = os.environ.get("DB_USER")
# db_pass = os.environ.get("DB_PASS")
# db_name = os.environ.get("DB_NAME")
# cloud_sql_connection_name = os.environ.get("CLOUD_SQL_CONNECTION_NAME")

# from sqlalchemy import create_engine
#   engine = create_engine('mysql+pymysql://DATABASE_USER:PASSWORD@127.0.0.1/DATABASE_NAME')
db = sqlalchemy.create_engine(
    # Equivalent URL:
    # mysql+pymysql://<db_user>:<db_pass>@/<db_name>?unix_socket=/cloudsql/<cloud_sql_instance_name>
    # Parameters
    #   drivername – the name of the database backend. This name will correspond to a module in sqlalchemy/databases or a third party plug-in.
    #   username – The user name.
    #   password – database password.
    #   host – The name of the host.
    #   port – The port number.
    #   database – The database name.
    #   query – A dictionary of options to be passed to the dialect and/or the DBAPI upon connect.
    sqlalchemy.engine.url.URL(
        drivername="mysql+pymysql",
        username=DB_USER,
        password=DB_PASS,
        database=DB_NAME,
        # query={"unix_socket": "/cloudsql/{}".format(CLOUD_SQL_CONNECTION_NAME)},
    ),
    pool_size=5,
    max_overflow=2,
    pool_timeout=30,  # 30 seconds
    pool_recycle=1800,  # 30 minutes
)

# with db.connect() as conn:
#     # Execute the query and fetch all results
#     recent_votes = conn.execute(
#         "select * from myasset.member_table"
#     ).fetchall()
#     print(recent_votes)

# 이 지점까지 테스트 성공
# Google Cloud SQL 데이터베이스에 '연결'하는 테스트 성공 (2020. 3. 18)

stmt = sqlalchemy.text(
    "select * from member_table"
)
try:
    # Using a with statement ensures that the connection is always released
    # back into the pool at the end of statement (even if an error occurs)

    # 이 지점에서 에러 발생.
    # 소켓 관련 에러 : "module 'socket' has no attribute 'AF_UNIX'"
    with db.connect() as conn:
        conn.execute(stmt)
except Exception as e:
    # If something goes wrong, handle the error in this section. This might
    # involve retrying or adjusting parameters depending on the situation.
    # [START_EXCLUDE]
    # logger.exception(e)
    print('Exception occurred!')
    print(e)
    # print e.args[0], e.args[1]
    # return None
except sqlalchemy.except_all as e:
    print('sqlalchemy Exception occurred!')
    print(e)
    # return None
except pymysql.err as e:
    print('pymysql Exception occurred!')
    print(e)
    # return None
finally:
    # conn.close()
    print('Finally Error!')

# conn = db.connect()