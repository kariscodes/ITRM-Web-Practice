#
# Succeed... using by sqlalchemy
#

import pymysql
import sqlalchemy
import os

DB_USER = "dev1"
DB_PASS = "dev2020"
DB_NAME = "das"
CLOUD_SQL_CONNECTION_NAME = "our-velocity-271006:us-west1:das"

# from sqlalchemy import create_engine
#   engine = create_engine('mysql+pymysql://DATABASE_USER:PASSWORD@127.0.0.1/DATABASE_NAME')

# Connected String: mysql+cymysql://<username>:<password>@<host>/<dbname>[?<options>]
# mysql+pymysql://<db_user>:<db_pass>@/<db_name>?unix_socket=/cloudsql/<cloud_sql_instance_name>
url = "mysql+pymysql://dev1:dev2020@34.82.158.37/myasset"
stmt = sqlalchemy.text(
    "select * from member_table"
)
try:
    engine = sqlalchemy.create_engine(url)
    with engine.connect() as conn:
        rows = conn.execute(stmt).fetchall()
except Exception as e:
    print(e)

print(rows)