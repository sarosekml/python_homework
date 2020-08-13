def some_func(some_a:float, some_b:float, some_c:int = 1) -> float:
    """ Calculate sum and raises a number to a power
    :param some_a: first argument
    :param some_b: second argument
    :param some_c: power (default = 1)
    :return:
    """
    result = (some_a + some_b) ** some_c
    return result

#print(some_func.__doc__)

#print(some_func(2, 4, 2))

print(some_func(some_a=2, some_b=4, some_c=2)) # поименная передача

"""встроенные функции
map
sorted
sum
min
max
zip
enumirate
range
"""

test_list = [2, 3, 4, 5, 6]

def my_f(x):
    return x ** 2 - 1
#
# test_list_res = []
# for itm test_list:
#     test_list_res.append(my_f(iym))

# def my_map(func, iter_obj):
#     result = []
#     for itm in iter_obj:
#         result.append(func(itm))
#     return result


# Пишем свой map
def my_map(func, iter_obj):
   for itm in iter_obj:
       yield func(itm)
    # yield 'end iter'

for  itm in my_map(my_f, test_list):
    print(itm)

# Пишем свой zip
list_a = [1, 2, 3, 4]
list_b = ['a', 'b', 'c', 'd']
list_c = [(1, 2), (3, 4), (5, 6), (7,8), (9, 10), (11, 12)]

list(zip(list_a, list_b, list_c))

def my_zip(*args):
    #print(type(args))
    idx = 0
    while True:
        result = []
        try:
            for itm in args:
                result.append(itm[idx])
        except IndexError:
            break
        yield tuple(result)
        idx += 1

# Пишем свой

def my_test(**kwargs):
    print(type(kwargs))

some_list = [1, 2, 3, 4, 5]

def some_list_appender(some_list: list):
    some_list.append('HELLO')
    return some_list
