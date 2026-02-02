import sys

if len(sys.argv) > 1:
    file = sys.argv[1]
else:
    raise Exception('Укажите имя файла: python solution.py file.txt')

with open(file, 'r', encoding='utf-8') as f:
    data = f.readlines()

result = []
for s in data:
    result.append(' '.join(s.split()[::-1]))

with open(file, 'w', encoding='utf-8') as f:
    f.write('\n'.join(result))