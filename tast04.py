def my_func(x, y):
    z = 1/(x**(-y))
    print(z)# вариант 1


    n = 1# вариант 2
    z = x
    while n < (-y):
        z = z * x
        n += 1

    print(1/z)

my_func(4, -3)