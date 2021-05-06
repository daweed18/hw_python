#   Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
#   Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
#   Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу:
#   длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * число см толщины
#   полотна. Проверить работу метода.
#   Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def weight(self):
        """ Функция считает вес асфальта

        :return: Вес асфальта (str)
        """
        return f"{self.__length * self.__width * 25 * 5 / 1000} т. "


route66 = Road(10000, 6)
print(route66.weight())