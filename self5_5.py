one = [1, 1, 3, 3, 1]
two = [5, 5, 5, 5, 5, 5, 5]
three = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]

def fix(list):
    result = set(list)
    for i in range(len(list)):
        count = list.count(list[i])
        if count > 1:
            x = str(list[i])
            for h in range(count - 1):
                x += str(list[i])
                result.add(x)
    print(result)

fix(one)
fix(two)
fix(three)