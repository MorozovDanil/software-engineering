one = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
two = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
three = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]

def fix(list):
    fixed = []
    for i in range(len(list)):
        if list[i] == 2:
            pass
        elif list[i] == 3:
            fixed.append(4)
        else:
            fixed.append(list[i])
    print(fixed)

fix(one)
fix(two)
fix(three)