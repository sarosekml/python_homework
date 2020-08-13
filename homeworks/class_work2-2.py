
my_list = [1, 2, 3, 'hello', True, False, [4, 5, 6]]  # список list(), зменяемы тип данных

my_tuple = (1, 2, 3, 'hello', True, False, [4, 5, 6])  # кортеж tuple(), неизменяемый тип данных

my_matrix = [[1,2,3], [4,5,6], [7,8,9]]

my_set = {1, 2, 3, 4, 5, 6, 'hello'}  # множество set(), изменяемый

my_frozenset = frozenset({1, 2, 3, 4, 5, 6, 'hello'})  # set(), НЕизменяемый

my_dict = {'key': 'hello', 1: [1, 2, 3, 4], 22.3: {1: 22}, True: (1, 2, 3)}  # словарь dict() изменяемы тип данных

# for idx, itm in enumerate(my_list, 1):
#     print(idx, '-', itm)


# for key, value in my_dict.items():
#     print(key, '-', value)

# for idx, value in enumerate(my_dict.values()):
#     print(value, idx)


for value in enumerate(my_set):
    print(value)