
def fun_divider(x, y):
    try:
        return x/y
    except ZeroDivisionError:
        print('Нельзя делить на ноль')
        return 0

def input_user(txt):
    while True:
        number = input(txt)
        if number.isdigit():
            return int(number)
        else:
            print('Вы ввели не число')

x = input_user('Введите делимое')
y = input_user('Введите делитель')

print(fun_divider(x, y))