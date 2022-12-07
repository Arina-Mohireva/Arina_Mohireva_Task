# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint

numbers = []

for i in range(16):
    numbers.append({
        "bin": bin(i), #задаем двоичное число
        "oct": oct(i), #задаем восьмеричное число
        "dec": i, #задаем десятичное число
        "hex": hex(i) #задаем шестнадцатеричное число
    })

pprint(numbers)


