# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию. Элементы
# вывести в порядке их следования в исходном списке. Для выполнения задания
# обязательно использовать генератор.

def new_list(some_list: list) -> list:
    """ Функция, принимающая список, создает список уникальных чисел

    some_list: список чисел
    """
    return [int(num) for num in some_list if some_list.count(num) == 1]


if __name__ == "__main__":
    user_list = input("Вводите числа через пробел: ").split()
    print(new_list(user_list))