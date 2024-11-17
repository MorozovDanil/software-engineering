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