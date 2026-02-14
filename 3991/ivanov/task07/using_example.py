import os
from solution import count_frequency

# Пример использования
file_text = "aaAAAbBBBBBbbcCCCc114432"

with open("test.txt", "w") as file:
    file.write(file_text)

# Проверяем несколько случаев
print("С учётом регистра:")
result = count_frequency("test.txt", ignore_case=False)
for ch, count in result.items():
    print(f"[{ch}]: {count}")
print()

print("Без учёта регистра:")
result = count_frequency("test.txt", ignore_case=True)
for ch, count in result.items():
    print(f"[{ch}]: {count}")
print()

print("В отсортированном порядке:")
result = count_frequency("test.txt", ignore_case=False, sort_output=True)
for ch, count in result:
    print(f"[{ch}]: {count}")
print()

# Очистка ресурсов
os.remove("test.txt")