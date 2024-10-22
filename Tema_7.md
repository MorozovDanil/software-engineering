# Тема 7.
Отчет по Теме #7 выполнил(а):
- Морозов Данил Алексеевич
- ИВТ-22-2

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |
| Задание 6 | + | - |
| Задание 7 | + | - |
| Задание 8 | + | - |
| Задание 9 | + | - |
| Задание 10 | + | - |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Лабораторная работа №1
### Составьте текстовый файл и положите его в одну директорию спрограммой на Python. Текстовый файл должен состоять минимум из двух строк.
### Результат.
![Меню](https://github.com/MorozovDanil/software-engineering/blob/Тема_7/pic/Lab7_1.png)

## Выводы

Файл сделал

## Лабораторная работа №2
### Напишите программу, которая выведет только первую строку из вашего файла, при этом используйте конструкцию open()/close().
```python
f = open('input.txt','r')
print(f.readline())
f.close()
```
### Результат.
![Меню](https://github.com/MorozovDanil/software-engineering/blob/Тема_7/pic/Lab7_2.png)

## Выводы

Выводит только первую строку

## Лабораторная работа №3
### Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию open()/close().
```python
f = open('input.txt','r')
print(f.readlines())
f.close()
```
### Результат.
![Меню](https://github.com/MorozovDanil/software-engineering/blob/Тема_7/pic/Lab7_3.png)

## Выводы

Выводит все строки в массиве

## Лабораторная работа №4
### Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию with open().
```python
with open('input.txt') as f:
    print(f.readlines())
```
### Результат.
![Меню](https://github.com/MorozovDanil/software-engineering/blob/Тема_7/pic/Lab7_4.png)

## Выводы

Выводит все строки в массиве

## Лабораторная работа №5
### Напишите программу, которая выведет каждую строку из вашего файла отдельно, при этом используйте конструкцию with open()
```python
with open('input.txt') as f:
    for line in f:
        print(line)
```
### Результат.
![Меню](https://github.com/MorozovDanil/software-engineering/blob/Тема_7/pic/Lab7_5.png)

## Выводы

Каждая строка отдельно

## Лабораторная работа №6
### Напишите программу, которая будет добавлять новую строку в ваш файл, а потом выведет полученный файл в консоль. Вывод можно осуществлять любым способом. Обязательно проверьте сам файл, чтобы изменения в нем тоже отображались.
```python
with open('input.txt','a+') as f:
    f.write('\nExtra text test')

with open('input.txt','r') as f:
    result = f.readlines()
    print(result)
```
### Результат.
![Меню](https://github.com/MorozovDanil/software-engineering/blob/Тема_7/pic/Lab7_6.png)

## Выводы

Добавляет строку в файл

## Лабораторная работа №7
###Напишите программу, которая перепишет всю информацию, которая была у вас в файле до этого, например напишет любые данные из произвольно вами составленного списка. Также не забудьте проверить что измененная вами информация сохранилась в файле```python

```
lines = {'one','two','three'}
with open('input.txt','w') as f:
    for line in lines:
        f.write('\nCycle run '+line)
    print('Done!')
```
### Результат.
![Меню](https://github.com/MorozovDanil/software-engineering/blob/Тема_7/pic/Lab7_7.png)

## Выводы

Переписывает данные в файле

## Лабораторная работа №8
### Выберите любую папку на своем компьютере, имеющую вложенные директории. Выведите на печать в терминал ее содержимое, как и всех подкаталогов при помощи функции print_docs(directory).
```python
import os

def print_docs(directory):
    all_files = os.walk(directory)
    for catalog in all_files:
        print(f'Папка {catalog[0]} содержит:')
    print(f'Директория {", ".join([folder for folder in catalog[1]])}')
    print(f'Файлы {", ".join([file for file in catalog[2]])}')
    print('-'*40)

print_docs('C:/Music/Dorian Electra - Fanfare (2023) [CD FLAC] {6922462566}')
```
### Результат.
![Меню](https://github.com/MorozovDanil/software-engineering/blob/Тема_7/pic/Lab7_8.png)

## Выводы

Выводит перечень файлов и каталогов в директории

## Лабораторная работа №9
### Требуется реализовать функцию, которая выводит слово, имеющее максимальную длину (или список слов, если таковых несколько). Проверьте работоспособность программы на своем наборе данных
```python
def longest_words(file):
   with open(file, encoding="utf-8") as f:
       words = f.read().split()
       max_lenght = len(max(words, key=len))
       for word in words:
           if len(word) == max_lenght:
               sought_words = word

       if len(sought_words) == 1:
           return sought_words[0]
       return sought_words


print(longest_words("input.txt"))
```
### Результат.
![Меню](https://github.com/MorozovDanil/software-engineering/blob/Тема_7/pic/Lab7_9.png)

## Выводы

Выводит слово с максимальной длинной

## Лабораторная работа №10
### Требуется создать csv-файл «rows_300.csv» со следующими столбцами: • № - номер по порядку (от 1 до 300); • Секунда – текущая секунда на вашем ПК; • Микросекунда – текущая миллисекунда на часах. Для наглядности на каждой итерации цикла искусственно приостанавливайте скрипт на 0,01 секунды.
```python
import csv, datetime, time

with open("rows_300.csv", "w", encoding="utf-8", newline="") as f:
   writer = csv.writer(f)
   writer.writerow(["№", "Sec", "Microsec"])
   for line in range(1,301):
       writer.writerow([line, datetime.datetime.now().second,
                        datetime.datetime.now().microsecond])
       time.sleep(0.01)
```
### Результат.
![Меню](https://github.com/MorozovDanil/software-engineering/blob/Тема_7/pic/Lab7_10.png)
![Меню](https://github.com/MorozovDanil/software-engineering/blob/Тема_7/pic/Lab7_10_1.png)

## Выводы

Создаёт CSV-файл

## Самостоятельная работа №1
### Найдите в интернете любую статью (объем статьи не менее 200 слов), скопируйте ее содержимое в файл и напишите программу, которая считает количество слов в текстовом файле и определит самое часто встречающееся слово. Результатом выполнения задачи будет: скриншот файла со статьей, листинг кода, и вывод в консоль, в котором будет указана вся необходимая информация.
```python
from collections import Counter

def word_count(file):
    result = 0
    with open(file,'r') as file:
        data = file.read()
        lines = data.split()
        result+=len(lines)
    print(result)

def most_said(file):
    with open(file, 'r') as file:
        data = file.read()
        split_it = data.split()
        most_occur = Counter(split_it).most_common(4)
    print(most_occur)

print(word_count('article.txt'),most_said('article.txt'))
```
### Результат.
![Меню](https://github.com/MorozovDanil/software-engineering/blob/Тема_7/pic/Self7_1.png)

## Выводы

Выводит самое повторяемое слово и кол-во слов

## Самостоятельная работа №2
### У вас появилась потребность в ведении книги расходов, посмотрев все существующие варианты вы пришли к выводу что вас ничего не устраивает и нужно все делать самому. Напишите программу для учета расходов. Программа должна позволять вводить информацию о расходах, сохранять ее в файл и выводить существующие данные в консоль. Ввод информации происходит через консоль. Результатом выполнения задачи будет: скриншот файла с учетом расходов, листинг кода, и вывод в консоль, с демонстрацией работоспособности программы.
```python
def remove(tpl, elem):
    if elem in tpl:
        elem_index = tpl.index(elem)
        return tpl[:elem_index] + tpl[elem_index + 1:]
    return tpl

print(remove((1, 2, 3), 1))
print(remove((1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3))
print(remove((2, 4, 6, 6, 4, 2), 9))
```
### Результат.
![Меню](https://github.com/MorozovDanil/software-engineering/blob/Тема_7/pic/Self7_2.png)

## Выводы

Позволяет вводить расходы 

## Самостоятельная работа №3
### Имеется файл input.txt с текстом на латинице. Напишите программу, которая выводит следующую статистику по тексту: количество букв латинского алфавита; число слов; число строк. • Текст в файле: Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated. • Ожидаемый результат: Input file contains: 108 letters 20 words 4 lines
```python
def result(file):
    with open(file) as infile:
        words = 0
        characters = 0
        for lineno, line in enumerate(infile, 1):
            wordslist = line.split()
            words += len(wordslist)
            characters += sum(len(word) for word in wordslist)

    print(lineno)
    print(words)
    print(characters)

result('poem.txt')
```
### Результат.
![Меню](https://github.com/MorozovDanil/software-engineering/blob/Тема_7/pic/Self7_3.png)

## Выводы

Выводит сколько строчек, букв и слов

## Самостоятельная работа №4
### апишите программу, которая получает на вход предложение, выводит его в терминал, заменяя все запрещенные слова звездочками. Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле input.txt. Все слова в этом файле записаны в нижнем регистре. Программа должна заменить запрещенные слова, где бы они ни встречались, даже в середине другого слова. Замена производится независимо от регистра.
```python
with open("censorship.txt", "r") as file:
   line = list(file.readline().split())

   input_str = ("Hello, world! Python IS the programming language of thE future. My EMAIL is...\n"
                "PYTHON is awesome")
   index_next_line = input_str.index("\n")
   print(index_next_line)
   input_list = input_str.split()

   for i in range(len(input_list)):
       for k in range(len(line)):
           if line[k] in input_list[i].lower():
               for j in line[k]:
                   input_list[i] = input_list[i].lower().replace(j, "*")

   out_string = ""
   for i in input_list:
       out_string += i + " "
       if len(out_string) == index_next_line + 1:
           out_string += "\n"
   print(out_string)
```
### Результат.
![Меню](https://github.com/MorozovDanil/software-engineering/blob/Тема_7/pic/Self7_4.png)

## Выводы

Убирает запрещённые слова

## Самостоятельная работа №5
###Создайте приложение которое позволяет скопировать данные из одного файла в другой
```python
def copy(file1,file2):
    with open(file1 ,'r') as firstfile, open(file2 ,'a') as secondfile:
        for line in firstfile:
            secondfile.write(line)


print('Файл из которого копируется:')
file1=input()
print('Файл из которого копируется:')
file2=input()
copy(file1,file2)
```
### Результат.
![Меню](https://github.com/MorozovDanil/software-engineering/blob/Тема_7/pic/Self7_5.png)
![Меню](https://github.com/MorozovDanil/software-engineering/blob/Тема_7/pic/Self7_5_1.png)
![Меню](https://github.com/MorozovDanil/software-engineering/blob/Тема_7/pic/Self7_5_2.png)

## Выводы

Программа даёт возможность копировать данные из одного файла в другой

## Общие выводы по теме

В выполненной работе были способы работы с файлами в Питоне