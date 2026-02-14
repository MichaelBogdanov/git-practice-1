import os


script_dir = os.path.dirname(os.path.abspath(__file__))
filename = input("Введите имя файла: ")
filepath = os.path.join(script_dir, filename)

with open(filepath, 'r', encoding='utf-8') as file:
    text = file.read()


words = text.split()
reversed_words = words[::-1]
result = ' '.join(reversed_words)

print(result)

