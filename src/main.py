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


chans = query_channels()
just_chans = [x[0] for x in chans]

subs = [x[1] for x in chans]
total_sum = sum(subs)

normal_subs = [x / total_sum for x in subs]

print(sum(normal_subs))
print(total_sum)

print(numpy.random.choice(just_chans, p=normal_subs))
