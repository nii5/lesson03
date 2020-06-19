
my_sum = 0
while True:
    str = input('Введите набор чисел через пробел')
    my_list = str.split(' ')
    stop = False
    for i in my_list:
        if i.isdigit():
            my_sum = my_sum + int(i)
        else:
            print(my_sum)
            stop = True
            break

    if stop:
        break
    else:
        print(f'Текущая сумма чисел {my_sum}')
print (f'Текущая сумма чисел {my_sum}')
