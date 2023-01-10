from datetime import datetime
ABR = 'files/abbreviations.txt'
ST = 'files/start.log'
END = 'files/end.log'


def convert_to_dict(x):
    with open(x, mode='r', encoding='utf-8') as file:
        onstring = file.readlines()
    st = {}
    for i in onstring:
        k = i[0:3]
        v = i[3:]
        v = v.strip()
        v = datetime.strptime(v, "%Y-%m-%d_%H:%M:%S.%f")
        st[k] = v
        return st


# Timedelta from dict end and st
def delta_dictionaries(x,y):
    res = {key: x[key] - y.get(key, 0) for key in x.keys()}
    return res


# Sort dictionary values
def sort_dictionary(res):
    sorted_res = sorted(res.items(), key=lambda x: x[1], reverse=True)
    sorted_res = dict(sorted_res)
    return sorted_res


if __name__ == "__main__":
    # Convert files to dictionary
    abr = convert_to_dict(ABR)
    st = convert_to_dict(ST)
    end = convert_to_dict(END)

# Timedelta result
res = delta_dictionaries(end, st)


# Building report by adding 2 dictionaries using keys
def build_report (x, y):
    report = {key: x[key] + y.get(key, 0) for key in x.keys()}

final = build_report(res, abr)


def print_report ():
    print(final)

print_report()
