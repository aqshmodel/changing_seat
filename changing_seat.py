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
    return seat


def save_seat(seat):
    file = open('previous_seat.txt', 'w')
    for i in range(0, 14):
        file.write(str(seat[i]) + '\n')
    file.write(str(seat[i+1]))
    file.close()


def exe_changing_seat(seat, join_member):
    f = open('previous_seat.txt', 'a')
    file = open('previous_seat.txt', 'r+')
    read_data = file.read().split()
    if read_data != [] and read_data.count == 15:
        join_member = read_data
        changing_seat(seat, join_member)
    else:
        changing_seat(seat, join_member)
    file.close()
    save_seat(seat)
