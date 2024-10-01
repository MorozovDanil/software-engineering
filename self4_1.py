from datetime import datetime #импорт функции datetime из модуля datetime
from math import sqrt #импорт функции sqrt из модуля math
def main(**kwargs): #функция main принимает специальный синтаксис **kwargs (в определениях функций в Python используется для передачи списка аргументов переменной длины с ключевыми словами)
    for key in kwargs.items(): #цикл for размером в количество элементов в kwargs
        result = sqrt(key[1][0] ** 2 + key[1][1] ** 2) #записываем результат вычислений в переменную
        print(result) #вывод результата
if __name__ == '__main__': #Основная функция
    start_time = datetime.now() #начало запуска программы
    main( #запуск функции main
    one=[10, 3], #параметры функции main
    two=[5, 4],
    three=[15, 13],
    four=[93, 53],
    five=[133, 15]
    )
    time_costs = datetime.now() - start_time #сколько времени заняли расчёты
    print(f"Время выполнения программы - {time_costs}") #Вывод сколько выполнялась программа