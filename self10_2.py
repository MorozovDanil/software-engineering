def check_file(name):
    try:
        f = open(name)
        f_str = f.readlines()
        f_str[0] = f_str[0]
        for i in f_str:
            print(i, end="")
    except:
        print("Файл пустой")
if __name__ == '__main__':
    check_file("test.txt")