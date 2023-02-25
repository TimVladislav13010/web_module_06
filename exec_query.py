import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect("users_hw.db") as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()
