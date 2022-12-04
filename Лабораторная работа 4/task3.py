def delete(list_, index=None):
    ...  # TODO реализовать функцию удаления элемента из списка по индексу

a = [0, 1, 2]
del a[0]
print(a)  # [0, 1]

a = [0, 1, 2]
del a[1:2]
print(a)  # [0, 2]

a = [0, 1, 2]
del a[-1]
print(a)  # [0, 1]
