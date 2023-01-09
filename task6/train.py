from datetime import datetime

ST = 'files/start.log'


def convert_to_dict(file):
    onstring = file.readlines()
    st = {}
    for i in onstring:
        k = i[0:3]
        v = i[3:]
        v = v.strip()
        v = datetime.strptime(v, "%Y-%m-%d_%H:%M:%S.%f")
        st[k] = v  # добавляем в словарь соответствующие пары ключ:значение


with open(ST, mode='r', encoding='utf-8') as fl:
        print(convert_to_dict(fl))


