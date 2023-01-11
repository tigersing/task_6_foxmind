from datetime import datetime

ABR = 'files/abbreviations.txt'
ST = 'files/start.log'
END = 'files/end.log'


def convert_to_dict(x, time_parser=False):
    with open(x, mode='r', encoding='utf-8') as file:
        on_string = file.readlines()
    st = {}
    for i in on_string:
        k = i[0:3]
        v = i[3:]
        v = datetime.strptime(v.strip(), "%Y-%m-%d_%H:%M:%S.%f") if time_parser else v
        st[k] = v
    return st


# Timedelta from dict end and st
def delta_dictionaries(x, y):
    return {key: (x[key] - y.get(key, 0)) for key in x.keys()}


# Sort dictionary values
def sort_dictionary(res):
    sorted_res = sorted(res.items(), key=lambda x: x[1].microseconds)
    sorted_res = dict(sorted_res)
    return sorted_res


def print_report():
    abr = convert_to_dict(ABR)
    st = convert_to_dict(ST, True)
    end = convert_to_dict(END, True)

    laps_data = sort_dictionary(delta_dictionaries(end, st))
    for k in laps_data.keys():
        _, name, team = abr[k].split('_')
        lap_time = laps_data[k]
        print(f"{name.strip()} | {team.strip()} | {str(lap_time)}")


if __name__ == "__main__":
    print_report()
