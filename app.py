'''
席替えアプリ

 ルール:
    - 席は15席あり、参加者は14名、TAが1名
    - 1つの席に1人しか着席できない
    - 1人は1つの席にしか着席できない
    - 必ず全員が着席しなければならない(15人いないとダメ)
    - TAも移動する
 希望度:
    - 参加者は毎回違う席に座ることを希望するが絶対ではない
    - 隣には違う人が座ることを希望するが絶対ではない
    - 隣同士になったことがない人が隣に来ることを希望するが絶対ではない
    - TAは上記希望の例外とする(工藤さんすみません)
'''
from changing_seat import exe_changing_seat

seat = list(range(1,16))
join_member = ['塚田崇博',
               '徳田貴一',
               '高橋通',
               '田中潤',
               '兼松智恵子',
               '熊谷航',
               '下川孝宣',
               '柴田雅幸',
               '中野英麿',
               '速水駿',
               '舞鶴翔',
               '望月千華子',
               '山田樹',
               '吉田力',
               '工藤響']


exe_changing_seat(seat,join_member)
