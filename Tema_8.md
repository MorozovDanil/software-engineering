# Тема 8.
Отчет по Теме #8 выполнил(а):
- Морозов Данил Алексеевич
- ИВТ-22-2

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |
| Задание 6 | - | - |
| Задание 7 | - | - |
| Задание 8 | - | - |
| Задание 9 | - | - |
| Задание 10 | - | - |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Лабораторная работа №1
###  Создайте класс “Car” с атрибутами производитель и модель. Создайте объект этого класса.
```python
class Car:
    def __init__(self,make,model):
        self.make = make
        self.model = model

my_car = Car("Toyota","Corolla")
```
### Результат.
![Меню](https://github.com/MorozovDanil/software-engineering/blob/Тема_8/pic/Lab8_1.png)

## Выводы

Создаётся объект класса

## Лабораторная работа №2
### Дополните код из первого задания, добавив в него атрибуты и методы класса, заставьте машину “поехать”.
```python
class Car:
    def __init__(self,make,model):
        self.make = make
        self.model = model

    def drive(self):
        print(f"Driving the {self.make} {self.model}")

my_car = Car("Toyota","Corolla")
my_car.drive()
```
### Результат.
![Меню](https://github.com/MorozovDanil/software-engineering/blob/Тема_8/pic/Lab8_2.png)

## Выводы

Машина "едет"

## Лабораторная работа №3
### Создайте новый класс “ElectricCar” с методом “charge” и атрибутом емкость батареи. Реализуйте его наследование от класса, созданного в первом задании. Заставьте машину поехать, а потом заряжаться.
```python
class Car:
    def __init__(self,make,model):
        self.make = make
        self.model = model

    def drive(self):
        print(f"Driving the {self.make} {self.model}")

class ElectricCar(Car):
    def __init__(self,make,model,battery_capacity):
        super().__init__(make,model)
        self.battery_capacity = battery_capacity

    def charge(self):
        print(f"Charging the {self.make} {self.model} with {self.battery_capacity} kWh")

    def drive(self):
        print(f"Driving the {self.make} {self.model}")

my_ElectricCar = ElectricCar("Tesla","Model S",75)
my_ElectricCar.charge()
my_ElectricCar.drive()
```
### Результат.
![Меню](https://github.com/MorozovDanil/software-engineering/blob/Тема_8/pic/Lab8_3.png)

## Выводы

Создаёт класс ElectricCar

## Лабораторная работа №4
### Реализуйте инкапсуляцию для класса, созданного в первом задании. Создайте защищенный атрибут производителя и приватный атрибут модели. Вызовите защищенный атрибут и заставьте машину поехать.
```python
class Car:
    def __init__(self,make,model):
        self._make = make
        self.__model = model

    def drive(self):
        print(f"Driving the {self._make} {self.__model}")

my_car = Car("Toyota","Corolla")
print (my_car._make)
# print(my_car.__model)
my_car.drive()
```
### Результат.
![Меню](https://github.com/MorozovDanil/software-engineering/blob/Тема_8/pic/Lab8_4.png)

## Выводы

Реализует инкапсуляцию для класса

## Лабораторная работа №5
### Реализуйте полиморфизм создав основной (общий) класс “Shape”, а также еще два класса “Rectangle” и “Circle”. Внутри последних двух классов реализуйте методы для подсчета площади фигуры. После этого создайте массив с фигурами, поместите туда круг и прямоугольник, затем при помощи цикла выведите их площади.
```python
class Shape:
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

r = 7
circle = Circle(r)
print(circle.area())

l = 5
w = 7
rectangle = Rectangle(l, w)
print(rectangle.area())
```
### Результат.
![Меню](https://github.com/MorozovDanil/software-engineering/blob/Тема_8/pic/Lab8_5.png)

## Выводы

Реализован полиморфизм

## Самостоятельная работа №1
### Самостоятельно создайте класс и его объект. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях.
```python
class Game:
    def __init__(self,title,price,rating):
        self.title = title
        self.price = price
        self.rating = rating

    def print_game(self):
        print(f"{self.title} is a {self.price} game that has a rating of {self.rating}")

Purchase = Game("Hollow Knight","7,49$","10/10")
Purchase.print_game()
```
### Результат.
![Меню](https://github.com/MorozovDanil/software-engineering/blob/Тема_8/pic/Self8_1.png)

## Выводы

Создан класс и его объект

## Самостоятельная работа №2
### Самостоятельно создайте атрибуты и методы для ранее созданного класса.
```python
class Game:
    def __init__(self,title,price,rating):
        self.title = title
        self.price = price
        self.rating = rating

    def print_game(self):
        print(f"{self.title} is a {self.price} game that has a rating of {self.rating}")

Purchase = Game("Hollow Knight","7,49$","10/10")
Purchase.print_game()
```
### Результат.
![Меню](https://github.com/MorozovDanil/software-engineering/blob/Тема_8/pic/Self8_2.png)

## Выводы

Есть методы и атрибуты

## Самостоятельная работа №3
### Самостоятельно реализуйте наследование, продолжая работать с ранее созданным классом
```python
class Game:
    def __init__(self,title,price,rating):
        self.title = title
        self.price = price
        self.rating = rating

    def print_game(self):
        print(f"{self.title} is a {self.price} game that has a rating of {self.rating}")

class Expansion(Game):
    def __init__(self,title,price,expansion_title):
        super().__init__(self,title,price)
        self.title = title
        self.expansion_title = expansion_title

    def print_expansion(self):
        print (f"{self.expansion_title} is an expansion for {self.title}. Coming soon!")

Purchase = Game("Hollow Knight","7,49$","10/10")
Purchase.print_game()
PurchaseExpansion = Expansion("Hollow Knight","12,99$","Silksong")
PurchaseExpansion.print_expansion()
```
### Результат.
![Меню](https://github.com/MorozovDanil/software-engineering/blob/Тема_8/pic/Self8_3.png)

## Выводы

Наследование класса Expansion от класса Game

## Самостоятельная работа №4
### Самостоятельно реализуйте инкапсуляцию, продолжая работать с ранее созданным классом
```python
class Game:
    def __init__(self,title,price,rating):
        self._title = title
        self._price = price
        self._rating = rating

    def print_game(self):
        print(f"{self._title} is a {self._price} game that has a rating of {self._rating}")

Purchase = Game("Hollow Knight","7,49$","10/10")
Purchase.print_game()
```
### Результат.
![Меню](https://github.com/MorozovDanil/software-engineering/blob/Тема_8/pic/Self8_4.png)

## Выводы

Реализована инкапсуляция

## Самостоятельная работа №5
###Самостоятельно реализуйте полиморфизм.
```python
class Animal:
    def sound(self):
        return "*Какой-то звук"

class Dog(Animal):
    def sound(self):
        return "Гав"

dog = Dog()
print(dog.sound())
```
### Результат.
![Меню](https://github.com/MorozovDanil/software-engineering/blob/Тема_8/pic/Self8_5.png)

## Выводы

Реализован полиморфизм

## Общие выводы по теме

В выполненной работе были основы ООП