def copy(file1,file2):
    with open(file1 ,'r') as firstfile, open(file2 ,'a') as secondfile:
        for line in firstfile:
            secondfile.write(line)


print('Файл из которого копируется:')
file1=input()
print('Файл из которого копируется:')
file2=input()
copy(file1,file2)