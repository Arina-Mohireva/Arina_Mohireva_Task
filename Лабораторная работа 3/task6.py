a = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
b = 0
for c in a:
    if c > b:
        b = c
x = [i for i, j in enumerate(a) if j == b]
k = x[-1]
a[k], a[-1] = a[-1], a[k]





# TODO Оформить решение

print(a)  # Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]
