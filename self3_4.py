value = input()
print(len(value),"\n",value.lower(),"\n",value.count('a')+value.count('e')+value.count('i')+value.count('o')+value.count('u'),"\n",value.replace("ugly","beauty"))
if value[:3]=='The' and value[-3:]=='end': print("Предложение начинается с The и заканчивается на end")