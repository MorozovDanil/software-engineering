val = int(input())
if 0 <= val <= 10:
    if (0<=val<=3): print('От 0 до 3 включительно')
    if (3<val<6): print('От 3 до 6')
    if (6<=val<=10): print('От 6 до 10 включительно')
else: print('Не подходит')