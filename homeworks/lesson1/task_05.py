'''Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение. Если фирма отработала с прибылью,
вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
'''

profit = int(input('Please enter proceeds (usd): '))
cost = int(input('Good! Now enter costs (usd): '))

if profit > cost:
    print('Good job! You work with profit')
    profitability = profit - cost
    print('Your profitability is ', profitability, 'usd')
    employee = int(input('How many employee work in your company? '))
    prof_per_employee = profitability / employee
    print('You profit per employee is ', prof_per_employee)
else:
    print('You should work hard to get profit :(')
