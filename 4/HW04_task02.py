'''
Напишите функцию, принимающую на вход только ключевые параметры и возвращающую словарь,
где ключ - значение переданного аргумента, а значение - имя аргумента. Если ключ не хешируем,
используйте его строковое представление
'''


def get_dict(**kwargs) -> dict:
    """Функция подготовки словаря из переданных аргументов и их значений"""
    result = {}
    for key, value in kwargs.items():
        try:
            result[value] = key
        except:
            result[str(value)] = key
    return result


if __name__ == "__main__":
    print("Исх. параметры: first=\"one\", second=2, third=3, fourth=\"four\", fifth=[2, 3]")
    print(get_dict(first="one", second=2, third=3, fourth="four", fifth=[2, 3]))

 