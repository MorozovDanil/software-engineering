def write_to_file(file,text):
    with open(file,'a+') as f:
        f.write(f'\n{text}')

def read_from_file(file):
    with open(file,'r') as f:
        result = f.readlines()
        print(result)

write_to_file('accounting.txt',input())
read_from_file('accounting.txt')