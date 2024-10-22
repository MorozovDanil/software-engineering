with open('input.txt','a+') as f:
    f.write('\nExtra text test')

with open('input.txt','r') as f:
    result = f.readlines()
    print(result)