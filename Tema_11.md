# Тема 10. Декораторы и исключения
Отчет по Теме #10 выполнил:
- Морозов Данил Алексеевич
- ИВТ-22-2

| Задание | Лаб_раб | Сам_раб |
| - | - | - |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

# Лабараторные работы 
## Лабараторная работа 1

  ```python
from functools import lru_cache
@lru_cache(None)
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)
if __name__ == '__main__':
    print(fib(496))
```
  ### Результат
  
 ![1](https://github.com/MorozovDanil/software-engineering/blob/Тема_10/pic/Lab10_1.png)

## Лабараторная работа 2

 ```python
def check(input_func):
    def output_func(*args):
        name, age = args[0], args[1],
        if age < 0 or age > 130:
            age = "Недопустимый возраст"
        input_func(name, age)
    return output_func
@check
def personal_info(name, age):
    print(f"Name: {name} Age: {age}")
if __name__ == '__main__':
    personal_info("Владимир", 38)
    personal_info("Александр", -5)
    personal_info("Петр", 131, 14, 1, 1, 1, 1, 1)

```

### Результат

![2](https://github.com/MorozovDanil/software-engineering/blob/Тема_10/pic/Lab10_2.png)

## Лабараторная работа 3

 ```python
def data(*args):
    try:
        for i in range(len(*args)):
            try:
                result = (args[0][i] * 15) // 10
                print(result)
            except Exception as ex:
                print(ex)
    except Exception as e:
        print(e)
    finally:
        print("Вся информация обработана")
if __name__ == '__main__':
    data([1, 15, "Hello", "I'm", "trying","to","crash","your","site", 38, 45])
```
### Результат

![3](https://github.com/MorozovDanil/software-engineering/blob/Тема_10/pic/Lab10_3.png)

## Лабараторная работа 4

 ```python
class NegativeValueException(Exception):
    pass

def check_name(name):
    if len(name) > 10:
        raise NegativeValueException("Длина более 10 символов")
    else:
        print("Успешная регистрация")
if __name__ == '__main__':
    name = "Данил"
    check_name(name)

```
### Результат

![4](https://github.com/MorozovDanil/software-engineering/blob/Тема_10/pic/Lab10_4.png)

## Лабараторная работа 5

 ```python
class SiteChecker:
    def __init__(self, func):
        print("Class SiteChecker метод __init__: запущен")
        self.func = func

    def __call__(self):
        print("Проверка перед запуском", self.func.__name__)
        self.func()
        print("Проверка безопасного выключения")


@SiteChecker
def site():
    print("Усердная работа сайта")


if __name__ == '__main__':
    print("Сайт запущен")
    site()
    print("Сайт выключен")

```
### Результат

![5](https://github.com/MorozovDanil/software-engineering/blob/Тема_10/pic/Lab10_5.png)


# Самостоятельные работы

## Самостоятельная работа №1

  ```python
import time
def fibonacci():
    fib1 = fib2 = 1
    for i in range(2, 200):
        fib1, fib2 = fib2, fib1 + fib2
        print(fib2, end=" ")
if __name__ == '__main__':
    a = time.time()
    fibonacci()
    b = time.time()
    print(f"\nПрограмма выполнялась {int((b - a) * 1000)} миллисекунд")

```

### Результат

![6](https://github.com/MorozovDanil/software-engineering/blob/Тема_10/pic/Self10_1.png)

## Краткий вывод:
Программа считает время начала выполнения функции и время.
 
## Самостоятельная работа №2

 ```python
def check_file(name):
    try:
        f = open(name)
        f_str = f.readlines()
        f_str[0] = f_str[0]
        for i in f_str:
            print(i, end="")
    except:
        print("Файл пустой")
if __name__ == '__main__':
    check_file("test.txt")

```

### Результат

![7](https://github.com/MorozovDanil/software-engineering/blob/Тема_10/pic/Self10_2.png)

## Краткий вывод:
Если файл пустой, то вызывается исключение и "файл пустой” выводится в консоль. Если он не пустой, то информацию из файла выводится в консоль.
## Самостоятельная работа №3

 ```python
def func(x):
    try:
        print(2 + int(x))
    except ValueError:
        print("Неподходящий тип данных. Ожидалось число")
if __name__ == '__main__':
    func(input("Введите число: "))

```

### Результат

![8](https://github.com/MorozovDanil/software-engineering/blob/Тема_10/pic/Self10_3.png)

## Краткий вывод:
Если пользователь введет строку или другой неподходящий тип данных, то в консоль выведется ошибка
## Самостоятельная работа №4

 ```python
def debug_decorator(func):
    def wrapper(*args):
        print(f"Вызов функции: {func.__name__}")
        print(f"Аргументы: {args[0], args[1]}")
        result = func(args[0], args[1])
        print(f"Результат: {result}")
        return result
    return wrapper
@debug_decorator
def addition(x, y):
    return x + y
@debug_decorator
def division(x, y):
    return x / y
if __name__ == '__main__':
    addition(11, 14)
    print()
    division(11, 14)

```

### Результат

![9](https://github.com/MorozovDanil/software-engineering/blob/Тема_10/pic/Self10_4.png)

## Краткий вывод:
Был реализован декоратор для дебага

## Самостоятельная работа №5

 ```python
class NegativeValueError(Exception):
    pass
def try_number(value):
    if value < 0:
        raise NegativeValueError(value)
    return value * 2
try:
    result = try_number(5)
    print(f"Результат обработки: {result}")
except NegativeValueError as e:
    print(f"Произошла ошибка: {e}")
try:
    result = try_number(-3)
    print(f"Результат обработки: {result}")
except NegativeValueError as e:
    print(f"Произошла ошибка: {e}")

```

### Результат

![10](https://github.com/MorozovDanil/software-engineering/blob/Тема_10/pic/Self10_5.png)

## Краткий вывод:

В программе был создан класс исключений

# Общий вывод 

Были изучены декораторы и исключения