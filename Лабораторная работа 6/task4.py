import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(input_file, a='\n', b=',') -> list[dict]:
    with open(input_file) as readfile:  # открываем фаил
        rows_ = readfile.read().split(a)  # разделяем фаил на строки
        str_ = [row.split(b) for row in rows_]  # разделяем строки
        dict_ = [dict(zip(str_[0], str_[i])) for i in range(1, len(rows_))]
    return dict_

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))

