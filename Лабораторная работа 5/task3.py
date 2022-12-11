from random import sample

def get_unique_list_numbers() -> list[int]:
    list_ = []  # создаем пустой список
    listt = sample(range(-10, 10), 15)  # генерируем случайные числа
    x = list_.append(listt)  # добавляем случайные числа в список
    return list_

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
# пустая строка
