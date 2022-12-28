from save_sql import read, Creating_table
import sqlite3
import time_get
from tqdm import tqdm
import operator

conn = sqlite3.connect('proxy.db')
cursor = conn.cursor()
listOfTables = cursor.execute(
    """SELECT name FROM sqlite_master WHERE type='table'
    AND name='PROXY'; """).fetchall()

dict = {}

if listOfTables:
    datas = read(cursor)
    Creating_table(cursor)
    # print(datas)
    for data in tqdm(datas):
        # print(data)
        connection = time_get.timed_check(data[1], int(data[2]), timeout=2)
        if connection.get("connect"):
            dict.update({(data[0],data[4]) : round(connection.get("time_get"),5)})
        query2 = f'''INSERT INTO connecting (connect, time_get, proxy_ID) VALUES ('{connection.get("connect")}','{connection.get("time_get")}','{data[0]}')'''
        cursor.execute(query2)


conn.commit()
conn.close()


sorted_dict = sorted(dict.items(), key=operator.itemgetter(1))
print(sorted_dict[:5])