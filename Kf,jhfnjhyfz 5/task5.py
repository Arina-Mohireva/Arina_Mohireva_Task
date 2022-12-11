import string
from random import sample


def get_random_password(n=None) -> str:
    if n is None:
        n = 8
    alpha_ = string.digits + string.ascii_letters  # создаем строку с нужными символами для генерации пароля
    pass_ = ''.join(sample(alpha_, n))  # генерируем пароль
    return pass_


print(get_random_password())
