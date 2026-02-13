import sys

def rotate_words(file: str):
    """Перевернуть порядок слов в тексте (и строк)"""
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    result = []
    
    for line in reversed(lines):
        line = line.strip()
        
        if line:
            words = line.split()
            reversed_words = ' '.join(words[::-1])
            result.append(reversed_words)
        else:
            result.append('')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(result))
          
if len(sys.argv) > 1:
    file = sys.argv[1]
    rotate_words(file)
else:
    raise Exception('Укажите имя файла: python solution.py file.txt')