def debug_decorator(func):
    def wrapper(*args):
        print(f"Вызов функции: {func.__name__}")
        print(f"Аргументы: {args[0], args[1]}")
        result = func(args[0], args[1])
        print(f"Результат: {result}")
        return result
    return wrapper
@debug_decorator
def addition(x, y):
    return x + y
@debug_decorator
def division(x, y):
    return x / y
if __name__ == '__main__':
    addition(11, 14)
    print()
    division(11, 14)