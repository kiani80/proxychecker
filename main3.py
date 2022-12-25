import time_get
from save_sql import save, Creating_table
import sqlite3

conn = sqlite3.connect('proxy.db')
cursor = conn.cursor()
Creating_table(cursor)


def analize_messages(link):
    try:
        details = link.split("?")[1].split("&")
        proxy={
            "link":link,
            details[0][:6] : details[0][7:],
            details[1][:4] : details[1][5:],
            details[2][:6] : details[2][7:],
        }
        connection = time_get.timed_check(proxy["server"],int(proxy["port"]),timeout=2)
        proxy.update(connection)
        return proxy
    except Exception as e:
        print(e , link)

def find_link(link,channal):
    
    data = analize_messages(link)
    if data:
        data.update({"channal":channal})
        save(cursor,data)
        conn.commit()

input_channals = input("Enter channals: ")
while(1):
    messages = input("Enter link: ")
    find_link(messages,input_channals)


conn.close()