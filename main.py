from divisor_master import prime, all_div, max_p_div, F, max_div
n = int(input('Введите целое число от 1 до 1000: '))

print('Число', n, 'является простым?', prime(n))
print('Список всех делителей', n,':', all_div(n))
print('Самый большой простой делитель', n, ':', max_p_div(n))
print('Каноническое разложение', n, 'на простые множители:', F(n))
print('Самый большой делитель', n, ':', max_div(n))