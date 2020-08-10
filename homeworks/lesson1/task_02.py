'''Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
'''

use_time_in_sec = int(input('Plese enter time in seconds: '))

hours = use_time_in_sec // 3600
minutes = (use_time_in_sec // 60) - (hours * 60)
second = use_time_in_sec - (hours * 3600) - (minutes * 60)

if hours < 10:
    hours = str(f'0{hours}')

if minutes < 10:
    minutes = str(f'0{minutes}')

if second < 10:
    second = str(f'0{second}')

print(f'Your time in hh:mm:ss format {hours}:{minutes}:{second}')