'''Поработайте с переменными, создайте несколько, выведите на экран,
запросите у пользователя несколько чисел и строк и сохраните в переменные,
выведите на экран.
'''

name = 'Mikhail'
surname = 'Sarosek'
age = 35

print('Hello, my name is ', name)
print('My surname is ', surname)
print("I'm ", age, "years old")

user_name = input('What is your name?')

print('OK! Nice to meet you,', user_name, '?')

user_surname = input('What is your surname?')
user_age = int(input(f'Good! How old are your, {user_name}?'))

print('Have a nice day, ', user_name, user_surname, user_age, 'years old!')