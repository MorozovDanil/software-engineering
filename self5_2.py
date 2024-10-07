my_list = [10.2, 14.8, 19.3, 22.7, 12.5, 33.1, 38.9, 21.6, 26.4, 17.1, 30.2, 35.7, 16.9, 27.8, 24.5, 16.3, 18.7, 31.9, 12.9, 37.4]
my_list.sort()
greater = []
greater.extend([i for i in my_list if i > 10])
print(f'Три лучшие:{my_list[-3:]}\nТри худшие:{my_list[:3]}\nВыше 10: {greater}')