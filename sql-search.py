import sqlite3
sql ={'AVG':"SELECT avg(number) FROM randomnumber", 'MAX':"SELECT max(number) FROM randomnumber", 'MIN': "SELECT \
    min(number) FROM randomnumber"}
pick = input("AVG or MAX on MIN or EXIT: ")
if pick != "EXIT":
    with sqlite3.connect("newnum.db") as conn:
        cursor = conn.cursor()
        cursor.execute(sql[pick])
        result = cursor.fetchone()
        print(pick + ":", result[0])
else:
    print("Exiting now")
    