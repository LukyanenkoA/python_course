#Требования для имени пользователя
#Имя пользователя может содержать буквы латинского алфавита (a–z), цифры (0–9).
#Запрещено использовать амперсанд (&), собаку(@), знаки равенства (=) и сложения (+), скобки (<>), запятую (,), апостроф ('), дефис (-)
#Количество символов должно быть от 8 до 20.
import re
valid_pattern = re.compile(r"^[a-z0-9]+$", re.I)

def check_name(name: str) -> bool:
    return bool(valid_pattern.match(name))
print(check_name("Am9h31d0jn"))
print(check_name("12"))
print(check_name("john@doe"))
'''
True
True
False
'''
def check_arg(username):
    try:
        if check_name(username):
            print(username)
        else:
            raise Exception('Ошибка ввода имени пользователя')
    except Exception:
        print('Необходимо ввести имя пользователя, соответствующее правилам!', username, 'не подходит')

check_arg("Am9h31d0jn")
check_arg("12")
check_arg("john@doe")
'''
Am9h31d0jn
12
Необходимо ввести имя пользователя, соответствующее правилам! john@doe не подходит
'''