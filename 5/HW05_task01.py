# 1. Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
#    Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.


LINK = "https://proprikol.ru/wp-content/uploads/2023/02/kartinki-s-dnem-pobedy-9-maya-5.jpg"


def split_path(path: str) -> tuple[str, str, str]:
    """Парсинг абсолютного пути на путь, имя и расширение файла"""
    path_only, *_, file_name = path.rpartition('/')
    file_name, _, file_ext = file_name.rpartition(".")
    return path_only, file_name, file_ext


def main():
    print(split_path(LINK))


if __name__ == "__main__":
    main()