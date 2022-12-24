import string
from random import sample

def get_random_password(n=8) -> str:
    pass_ = ''.join(sample(string.digits + string.ascii_letters, n))  # генерируем пароль
    return pass_

print(get_random_password())
