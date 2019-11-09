import sqlite3
from contextlib import closing

dbname = 'changing_seat.db'

with closing(sqlite3.connect(dbname)) as conn:
    c = conn.cursor()

    c.execute('create table members(id int, name varchar(64),previous_seat int, this_time_seat int,previous_buddy int, this_time_buddy int, satisfaction_level int)')

    # SQL文に値をセットする場合は，Pythonのformatメソッドなどは使わずに，
    # セットしたい場所に?を記述し，executeメソッドの第2引数に?に当てはめる値を
    # タプルで渡す．
    sql = 'insert into members (id, name, previous_seat, this_time_seat,previous_buddy,this_time_buddy,satisfaction_level) values (?,?,?,?,?,?,?)'
    user = (1, '塚田崇博', 1, 5, 8, 9, 3)
    c.execute(sql, user)

    # 一度に複数のSQL文を実行したいときは，タプルのリストを作成した上で
    # executemanyメソッドを実行する
    # insert_sql = 'insert into users (id, name, age, gender) values (?,?,?,?)'
    # users = [
    #     (2, 'Shota', 54, 'male'),
    #     (3, 'Nana', 40, 'female'),
    #     (4, 'Tooru', 78, 'male'),
    #     (5, 'Saki', 31, 'female')
    # ]
    # c.executemany(insert_sql, users)
    conn.commit()

    select_sql = 'select * from members'
    for row in c.execute(select_sql):
        print(row)