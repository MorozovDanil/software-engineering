def data(*args):
    try:
        for i in range(len(*args)):
            try:
                result = (args[0][i] * 15) // 10
                print(result)
            except Exception as ex:
                print(ex)
    except Exception as e:
        print(e)
    finally:
        print("Вся информация обработана")
if __name__ == '__main__':
    data([1, 15, "Hello", "I'm", "trying","to","crash","your","site", 38, 45])