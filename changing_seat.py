import random


def changing_seat(seat,join_member):
    random.shuffle(join_member)
    print('---- Aテーブル ----')
    for i in range(0, 15):
        seat[i] = join_member[i]
        print(str(i + 1) + 'の席:' + join_member[i])
        if i == 3:
            print('---- Bテーブル ----')
        elif i == 8:
            print('---- Cテーブル ----')


