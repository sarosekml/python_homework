'''Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.'''

user_num = int(input('Please enter natural number above zero: '))

if user_num < 0:
    print('Your number below zero, goodbye!')

else:
    maximus = user_num % 10

    while user_num > 0:
        if user_num % 10 > maximus:
            maximus = user_num
        else:
            user_num = user_num // 10

    print('Maximum number from your input is ', maximus)

#note: how to make this task repeatable?