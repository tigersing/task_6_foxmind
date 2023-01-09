from datetime import datetime
ABR = 'files/abbreviations.txt'
ST = 'files/start.log'
END = 'files/end.log'


def convert_to_dict(x):
    file = with open(x, mode='r', encoding='utf-8') as file_2:
    onstring = file.readlines()
    st = {}
    for i in onstring:
        k = i[0:3]
        v = i[3:]
        v = v.strip()
        if not v.isalpha() :
            v = datetime.strptime(v, "%Y-%m-%d_%H:%M:%S.%f")
        else:
            return v
        st[k] = v # добавляем в словарь соответствующие пары ключ:значение

# Convert files to dictionary
abr = convert_to_dict(ABR)
st = convert_to_dict(ST)
end = convert_to_dict(END)


# Timedelta from dict end and st
def delta_dictionaries(x,y):
    res = {key: end[key] - st.get(key, 0) for key in end.keys()}
    return res

# Sort dictionary values
def sort_dictionary():
    sorted_res = sorted(res.items(), key=lambda x:x[1],      reverse=True)
    sorted_res = dict(sorted_res)
    return sorted_res

# Convert timedelta into string
def sort_dictionary():
    res = dict()
    for sub in sorted_res:
            res[sub] = str(sorted_res[sub])
        return res



if name == "main":
    def combine_dictionaries(x, y):
        final = {}
        final = {key: res[key] + abr.get(key, 0) for key in res.keys()}
        return final

    def print_report():
        print(final)