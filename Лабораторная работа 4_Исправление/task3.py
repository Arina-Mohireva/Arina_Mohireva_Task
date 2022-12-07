def delete(item_list, idx=None):
    if idx is None:  # делаем так, чтоб по умолчанию удалялся последний элемент
        idx = -1
        result = item_list[:idx]
        return result

    if abs(idx) > len(item_list):
        print("Индекс за рамками массива")
        return item_list

    if idx < 0: # если индекс присутствует, то пользуемся слайсированием
        idx = len(item_list) + idx

    result = item_list[:idx] + item_list[(idx + 1):]  # соединяем списки
    return result


print(delete([0, 1, 2], idx=0))  # [1, 2]
print(delete([0, 1, 2], idx=1))  # [0, 2]
print(delete([0, 1, 2], idx=-1))  # [0, 1]
