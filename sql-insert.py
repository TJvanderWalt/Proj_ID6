import random
import sqlite3
rand_num = [(i, random.randint(1,100)) for i in range(1, 1000)]
with sqlite3.connect("newnum.db") as conn:
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE randomnumber (count INTEGER, number INTEGER)""")
    cursor.executemany('INSERT INTO randomnumber VALUES(?,?)',rand_num)
