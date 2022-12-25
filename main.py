from tel_connect import get_proxy
import time_get
from save_sql import save, Creating_table
import sqlite3

conn = sqlite3.connect('proxy.db')
cursor = conn.cursor()
Creating_table(cursor)

channals = ["https://t.me/DeamNet_proxy","https://t.me/MTP_roto"]

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

def find_link(messages,channal):
    if channal == "https://t.me/DeamNet_proxy":
        for text in messages:
            links = text.split()
            for link in links:
                data = analize_messages(link)
                if data:
                    data.update({"channal":channal})
                    save(cursor,data)
    if channal == "https://t.me/MTP_roto":
        for text in messages:
            link = text.split("(")[1].split(")")[0]
            data = analize_messages(link)
            if data:
                data.update({"channal":channal})
                save(cursor,data)
            
    conn.commit()

for channal in channals:

    messages = []
    get_proxy(messages,channal)
    find_link(messages,channal)

    # می تونی برای کانال های جدید کرالر جدید بنویسی
    #  می تونی درمورد اینکه چه تعداد پیام اخر کانال را بخواند فکر کنی و حالتش رو کامل کنی


conn.close()