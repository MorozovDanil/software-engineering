def remove(tpl, elem):
    if elem in tpl:
        elem_index = tpl.index(elem)
        return tpl[:elem_index] + tpl[elem_index + 1:]
    return tpl

print(remove((1, 2, 3), 1))
print(remove((1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3))
print(remove((2, 4, 6, 6, 4, 2), 9))