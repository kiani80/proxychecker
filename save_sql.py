def Creating_table(cursor):
    table = '''CREATE TABLE IF NOT EXISTS PROXY(
            ID 	     INTEGER PRIMARY KEY AUTOINCREMENT,
            server   TEXT    NOT NULL,
            port     TEXT    NOT NULL,
            key      TEXT    NOT NULL,
            link     TEXT    NOT NULL,
            channal  TEXT
            );'''
            # disconnect  boolean NOT NULL DEFAULT false,

    table2 = '''CREATE TABLE IF NOT EXISTS connecting(
            ID 	      INTEGER PRIMARY KEY AUTOINCREMENT,
            connect   TEXT,
            time_get  TEXT,
            proxy_ID  INTEGER,
            FOREIGN KEY(proxy_ID) REFERENCES PROXY(ID)
            );'''
            # time      datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,

    cursor.execute(table)
    cursor.execute(table2)


def save(cursor, proxy):
    query3 = f'''SELECT * FROM PROXY WHERE server = "{proxy.get("server")}"'''
    cursor.execute(query3)
    output = cursor.fetchall()
    if output:
        return
    query2 = f'''INSERT INTO PROXY (server, port, key, link, channal) VALUES ('{proxy.get("server")}','{proxy.get("port")}','{proxy.get("secret")}','{proxy.get("link")}','{proxy.get("channal")}');'''
    cursor.execute(query2)

    id = cursor.execute(f'''SELECT ID FROM PROXY WHERE server = "{proxy.get("server")}"''').fetchone()[0]
    query = f'''INSERT INTO connecting (connect, time_get, proxy_ID) VALUES ('{proxy.get("connect")}','{proxy.get("time_get")}','{id}')'''
    cursor.execute(query)


def read(cursor):
    data = cursor.execute('''SELECT * FROM PROXY''').fetchall()
    return data