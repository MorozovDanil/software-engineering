import random

def roll(num):
    match num:
        case 1:
            print('Вы проиграли')
        case 2:
            print('Вы проиграли')
        case 3:
            roll(random.randint(1,6))
        case 4:
            roll(random.randint(1, 6))
        case 5:
            print('Вы победили')
        case 6:
            print('Вы победили')

if __name__ == '__main__':
    roll(random.randint(1, 6))