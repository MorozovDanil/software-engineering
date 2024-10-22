from collections import Counter

def word_count(file):
    result = 0
    with open(file,'r') as file:
        data = file.read()
        lines = data.split()
        result+=len(lines)
    print(result)

def most_said(file):
    with open(file, 'r') as file:
        data = file.read()
        split_it = data.split()
        most_occur = Counter(split_it).most_common(4)
    print(most_occur)

print(word_count('article.txt'),most_said('article.txt'))