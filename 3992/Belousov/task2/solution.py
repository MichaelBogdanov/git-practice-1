def function1():
    file = open("text.txt")
    text = file.read()
    file.close()

    text_better = text.split()
    maxim = max(text_better, key=len)
    if maxim[-1]=='.' or maxim[-1]==',' : maxim = maxim[:-1]

    return f"Count of words: {len(text_better)}, string count: {text.count('.')}, most long word: {maxim}, it's length - {len(maxim)} letters"

print(function1())