import os
from solution import clear_file

# Пример использования
file_text = "the code random the the code random the code random"

with open("test.txt", "w") as file:
    file.write(file_text)

result = clear_file("test.txt")
print(f"{result=}")
# Ожидаемый результат: 'the core random'

# Очистка ресурсов
os.remove("test.txt")