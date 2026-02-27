import sys

def main():
    # Проверка указан ли файл
    if len(sys.argv) != 2:
        print ("используется: <файл>")
        return
    
    # читает файл
    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        text = f.read()

    # разбивает на слова и удаляет пробелы
    words = text.split()

    # переворачивает 
    words.reverse()

    # соединяем с 1 пробелом 
    result = ' '.join(words)

    print(result)

if __name__ == "__main__":
    main()
    