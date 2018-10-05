import psycopg2
import numpy


def query_channels():
    conn = psycopg2.connect(user='root', password='', host='127.0.0.1', port='5432', database='youtube')
    sql = f'SELECT chan_serial, subs FROM youtube.channels.chans ORDER BY subs DESC'
    cursor = conn.cursor()
    cursor.execute(sql)
    records = [x for x in cursor.fetchall()]

    cursor.close()
    conn.close()

    return records


for c in query_channels():
    print(c)
