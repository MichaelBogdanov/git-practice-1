import os
from solution import compress_RLE, decompress_RLE

# Пример использования
file_text = "HHHHHeeellllooooo Wooooorrrrlllldddd!!!! 555555"

with open("input.txt", 'w') as file:
    file.write(file_text)

compress_RLE("input.txt", "compressed.txt")
decompress_RLE("compressed.txt", "decompressed.txt")

with open("decompressed.txt", 'r') as file:
    decompressed_text = file.read()

print(f"Original text: {file_text}")
print(f"Compressed text: {decompressed_text}")
assert file_text == decompressed_text

# Очистка ресурсов
os.remove("input.txt")
os.remove("compressed.txt")
os.remove("decompressed.txt")