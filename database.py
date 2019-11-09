import sqlite3
from contextlib import closing

dbname = 'changing_seat.db'

with closing(sqlite3.connect(dbname)) as conn:
    c = conn.cursor()

    #
    # insert_sql = 'insert into members (id, name, previous_seat, this_time_seat,previous_buddy,this_time_buddy,satisfaction_level) values (?,?,?,?,?,?,?)'
    # users = [
    #      (2, '田中潤', 2, 1, 9, 3, 2),
    #      (3, '高橋通', 10,6, 11,2, 1),
    #  ]
    # c.executemany(insert_sql, users)
    #
    # conn.commit()

    select_sql = 'select * from members where id=4'
    for row in c.execute(select_sql):
        print(row)
