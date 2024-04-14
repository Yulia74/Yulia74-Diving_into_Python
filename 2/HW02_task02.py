''' Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение  дробей.
Для проверки своего кода используйте модуль fractions'''

from fractions import Fraction
import math


str_1 = input("Введите 1-ю дробь типа a/b: ")
str_2 = input("Введите 2-ю дробь типа a/b: ")

def shortenFraction(n: int, m: int):                    # метод сокращения дроби
    if n > m:
        k = n
    else:
        k = m
    while k != 1:
        if n % k == 0 and m % k == 0:
            return str(n // k) + "/" + str(m // k)
        else:
            k -= 1
    return str(n) + "/" + str(m)

def Get_sum(str_1, str_2):                        # метод сложения двух дробей
    num_1 = str_1.split("/")
    num_2 = str_2.split("/")
    lcm_fraction = math.lcm(int(num_1[1]), int(num_2[1]))   # НОЗ дроби
    numeratorFraction_1 = int(lcm_fraction / int(num_1[1]) * int(num_1[0]))
    numeratorFraction_2 = int(lcm_fraction / int(num_2[1]) * int(num_2[0]))
    return shortenFraction(numeratorFraction_1 + numeratorFraction_2, lcm_fraction)

def Get_mult(str1, str2):                          # метод умножения двух дробей
    num_1 = str1.split("/")
    num_2 = str2.split("/")
    
    return shortenFraction(int(num_1[0]) * int(num_2[0]), int(num_1[1]) * int(num_2[1]))

print("Расчет программы без модуля fraction:")
print(f'{str_1} * {str_2} = {Get_mult(str_1, str_2)}')
print(f'{str_1} + {str_2} = {Get_sum(str_1, str_2)}')

print("\nРешение с помощью модуля fraction:")

print(f"{str_1} * {str_2} = {Fraction(int(str_1.split('/')[0]), int(str_1.split('/')[1])) * Fraction(int(str_2.split('/')[0]), int(str_2.split('/')[1]))}")
print(f"{str_1} * {str_2} = {Fraction(int(str_1.split('/')[0]), int(str_1.split('/')[1])) + Fraction(int(str_2.split('/')[0]), int(str_2.split('/')[1]))}")
