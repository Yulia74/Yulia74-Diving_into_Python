'''Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
Программа должна подсказывать “больше” или “меньше” после каждой попытки.'''

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1_001
COUNT_TRY = 10

num = randint(LOWER_LIMIT, UPPER_LIMIT)

while True:
    my_num = int(input('Введите число от 0 до 1_000: '))
    if 0 <= my_num <= 1_000:
        break

for _ in range(COUNT_TRY - 1):
    if my_num != num:
        if my_num > num:
            print('Меньше')
            my_num = int(input())
        else:
            print('Больше')
            my_num = int(input())
    if my_num == num:
        print('Угадал!')
        break
else:
    print('Превышен лимит попыток (10), загаданное число = ', num)

