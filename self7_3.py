def result(file):
    with open(file) as infile:
        words = 0
        characters = 0
        for lineno, line in enumerate(infile, 1):
            wordslist = line.split()
            words += len(wordslist)
            characters += sum(len(word) for word in wordslist)

    print(lineno)
    print(words)
    print(characters)

result('poem.txt')