
def my_func(x, y, z):
    my_list = [x, y, z]
    my_list.remove(min(x, y, z))
    return sum(my_list)

print(my_func(10, 12,7))