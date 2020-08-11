'''Узнайте у пользователя число n.
Найдите сумму чисел n + nn + nnn. \
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
'''

number_n = int(input('Please, enter your number'))

nn = str(f'{number_n}{number_n}')
nn = int(nn)

nnn = str(f'{number_n}{number_n}{number_n}')
nnn = int(nnn)

number_sum = number_n + nn + nnn

print(number_sum)