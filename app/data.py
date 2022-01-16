import sys

from psycopg2 import connect, Error
from psycopg2.extras import execute_values


db_name = 'database'
db_user = 'dbuser'
db_pass = 'dbpass'
db_host = 'db'
db_port = '5432'

try:
    conn = connect(
        host=db_host,
        user=db_user,
        password=db_pass,
        port=db_port,
        database=db_name,
    )
    cur = conn.cursor()
except (Exception, Error) as err:
    print("\npsycopg2 connect error:", err)
    conn = None
    cur = None
    sys.exit(1)


def data_mapping(x):
    return {
        'meta_data': 'TEXT',
        'text': 'TEXT',
        'number': 'DOUBLE PRECISION'
    }.get(x)


def create_table(table_name, columns):
    sql_create_tbl = ""
    for column in columns:
        sql_create_tbl += f"{column[0]} {data_mapping(column[1])}, "
    sql_create_tbl = sql_create_tbl.rstrip(' ,')
    query_str = f'CREATE TABLE IF NOT EXISTS {table_name} ({sql_create_tbl});'
    try:
        cur.execute(query_str)
        print(f"Successfully created table {table_name}")
    except(Exception, Error) as error:
        print("\ncreate_table() error:", error)
        conn.rollback()
        sys.exit(1)


def insert_batch(table_name, columns, data):
    columns_str = ""
    for column in columns:
        columns_str += column[0] + ', '
    columns_str = columns_str.rstrip(', ')
    query_sql = f"INSERT INTO {table_name} ({columns_str}) VALUES %s"
    try:
        execute_values(cur,
                       query_sql,
                       data,
                       page_size=2000)
        conn.commit()
        print(f"Successfully inserted the data into {table_name}")
    except (Exception, Error) as error:
        print("\ninsert_batch() error:", error)
        conn.rollback()
        sys.exit(1)


def get_number_of_records(table_name):
    query = f"SELECT COUNT(*) FROM {table_name};"
    try:
        cur.execute(query)
        count = cur.fetchone()
    except (Exception, Error) as error:
        print("\nget_number_of_records() error:", error)
        conn.rollback()
        sys.exit(1)
    return count


def get_last_ten(table_name):
    query = f"SELECT * FROM {table_name} ORDER BY sid DESC LIMIT 10;"
    try:
        cur.execute(query)
        rows = cur.fetchall()

    except (Exception, Error) as error:
        print("\nget_number_of_records() error:", error)
        conn.rollback()
    return rows
