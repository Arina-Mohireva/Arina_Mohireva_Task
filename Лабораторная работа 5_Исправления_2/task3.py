import random

def get_unique_list_numbers(a=-10, b=10, c=15):
  list_ = []
  count = 0

  while count != c:  # задаем количество символов
    number = random.randint(a, b)  # генерируем числа
    if number not in list_:  # проверяем уникальность
      list_.append(number)  # если уникальное, добавляем в список
      count += 1  # добавляем значения уникальных символов в счетчик
  return list_

print(get_unique_list_numbers)

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
