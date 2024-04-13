# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

BASE = 16

num = int(input('Введите число: '))

print(hex(num))

num_hexadecimal = ''

while num:                             
 
    if num % BASE == 10:
        num_hexadecimal += str('a')
    elif str(num % BASE) == '11':
         num_hexadecimal += str('b')
    elif str(num % BASE) == '12':
         num_hexadecimal += str('c')
    elif str(num % BASE) == '13':
         num_hexadecimal += str('d')
    elif str(num % BASE) == '14':
         num_hexadecimal += str('e')
    elif str(num % BASE) == '15':
         num_hexadecimal += str('f')
    else:
         num_hexadecimal += str(num % BASE)
    
    num //= BASE

print(f'  {num_hexadecimal[::-1]}')
