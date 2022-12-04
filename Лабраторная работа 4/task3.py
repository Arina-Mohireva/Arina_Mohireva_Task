def delete(a, x=None):
    if x is None:  # делаем так, чтоб по умолчанию удалялся последний элемент
        x = -1
        b = a[:x]
    else:  # если индекс присутствует, то пользуемся слайсированием
        b = a[:x] + a[(x + 1):]  # соединяем списки
    return b


print(delete([0, 1, 2], x=0))  # [0, 1]
print(delete([0, 1, 2], x=1))  # [0, 2]
print(delete([0, 1, 2]))  # [0, 1]
