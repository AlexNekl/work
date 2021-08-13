# Задание № 1:
# Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:

seconds = int(input('Введите количество секунд: '))
minutes = (seconds // 60)
hours = (minutes // 60)
days = (hours // 24)
if seconds < 60:
   print(seconds, 'сек.')
elif minutes < 60:
   print(minutes, 'мин.', seconds % 60, 'сек.')
elif hours < 24:
   print(hours, 'час.', minutes % 60, 'мин.', seconds % 60, 'сек.')
elif days < 1:
    print(hours % 24, 'час.', minutes % 60, 'мин.', seconds % 60, 'сек.')
else:
   days > 1
   print(days, 'дн.', hours % 24, 'час.', minutes % 60, 'мин.', seconds % 60, 'сек.')


# Задание № 2:
# Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
# Внимание: использовать только арифметические операции!
# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
# сумма цифр которых делится нацело на 7

sum1 = 0
sum2 = 0
odd_numbers = []
for i in range(1, 1000, 2):
    odd_numbers.append(i**3)

for n in odd_numbers:

    number = n
    sum_of_digits = 0

    while number != 0:
        sum_of_digits += number % 10
        number //= 10
    if sum_of_digits % 7 == 0:
        sum1 += n
print(sum1)

for n in odd_numbers:

    n += 17
    number = n
    sum_of_digits = 0

    while number != 0:
        sum_of_digits += number % 10
        number //= 10
    if sum_of_digits % 7 == 0:
        sum2 += n
print(sum2)

# Задание № 3:
# Реализовать склонение слова «процент» во фразе «N процентов».
# Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:

for i in range(1, 101):
    if i == 0 or i % 10 == 0:
        print(i, 'процентов')
    elif i >= 11 and i <= 14:
        print(i, 'процентов')
    elif i % 10 >= 2 and i % 10 <= 4:
        print(i, 'процента')
    elif i % 10 >= 5 and i % 10 <= 9:
        print(i, 'процентов')
    elif i % 10 == 1:
        print(i, 'процент')
