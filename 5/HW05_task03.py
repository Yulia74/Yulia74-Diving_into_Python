# 3.  Создайте функцию генератор чисел Фибоначчи

member = int(input('Введите количество чисел в последовательности Фибоначчи: '))


def fib_gen(n: int) -> list[int]:
    """Генератор чисел Фибоначчи"""
    fib_list = [0]
    fib1 = 0
    fib2 = 1
    for _ in range(n):
        fib_list.append(fib2)
        fib1, fib2 = fib2, fib2 + fib1
    yield fib_list


def main():
    print(*fib_gen(member))


if __name__ == "__main__":
    main()