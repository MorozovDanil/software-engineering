# Тема 11. Итераторы и генераторы
Отчет по Теме #11 выполнил:
- Морозов Данил Алексеевич
- ИВТ-22-2

| Задание | Лаб_раб | Сам_раб |
| - | - | - |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | - |
| Задание 4 | + | - |
| Задание 5 | + | - |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

# Лабораторные работы 
## Лабораторная работа 1

  ```python
nums = [0, 1, 2, 3, 4, 5]
for item in nums:
  print(item)
```
  ### Результат
  
 ![1](https://github.com/MorozovDanil/software-engineering/blob/Тема_11/pic/Lab11_1.png)

## Лабораторная работа 2

 ```python
class CountDown:
   def __init__(self, start):
       self.count = start + 1

   def __iter__(self):
       return self

   def __next__(self):
       self.count -= 1
       if self.count < 0:
           raise StopIteration
       return self.count


if __name__ == '__main__':
   counter = CountDown(5)
   for i in counter:
       print(i)

```

### Результат

![2](https://github.com/MorozovDanil/software-engineering/blob/Тема_11/pic/Lab11_2.png)

## Лабораторная работа 3

 ```python
class CountDown:
   def __init__(self, start):
       self.count = start + 1

   def __iter__(self):
       return self

   def __next__(self):
       self.count -= 1
       if self.count < 0:
           raise StopIteration
       return self.count


if __name__ == '__main__':
   counter = CountDown(5)
   for i in counter:
       print(i)
```
### Результат

![3](https://github.com/MorozovDanil/software-engineering/blob/Тема_11/pic/Lab11_3.png)

## Лабораторная работа 4

 ```python
b = (i ** 2 for i in range(1, 5))
print(b)
for i in b:
   print(i)
print("second")


for i in b:
   print(i)
```
### Результат

![4](https://github.com/MorozovDanil/software-engineering/blob/Тема_11/pic/Lab11_4.png)

## Лабораторная работа 5

 ```python
def countdown(count):
   while count >= 0:
       yield count
       count -= 1


if __name__ == '__main__':
   counter = countdown(5)
   for i in counter:
       print(i)
```
### Результат

![5](https://github.com/MorozovDanil/software-engineering/blob/Тема_11/pic/Lab11_5.png)


# Самостоятельные работы

## Самостоятельная работа №1

  ```python
	def fib(n):
	  f_n, f_n1 = 1, 1
	  for i in range(n):
		  yield f_n
		  f_n, f_n1 = f_n1, f_n1 + f_n

	n = 321
	f_list = list(fib(n))
	print(f_list[-1])
```

### Результат

![6](https://github.com/MorozovDanil/software-engineering/blob/Тема_11/pic/Self11_1.png)

## Краткий вывод:
Генератор сокращает используемые программой ресурсы
 
## Самостоятельная работа №2

 ```python
def fib(n):
   f_n, f_n1 = 1, 1
   with open("fib.txt", "w") as file:
       for i in range(n):
           file.write(f"{f_n}\n")
           yield f_n
           f_n, f_n1 = f_n1, f_n1 + f_n


n = 321
f_list = list(fib(n))
print(f_list[-1])
```

### Результат

![7](https://github.com/MorozovDanil/software-engineering/blob/Тема_11/pic/Self11_2.png)

## Краткий вывод:
Как первый случай, но записываются построчно в файл

# Общий вывод 

Были изучены итераторы и генераторы