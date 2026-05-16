def reverse_words(text):
    words = text.split()
    return ' '.join(reversed(words))


input_file = "input.txt"
output_file = "output.txt"

with open(input_file, "r", encoding="utf-8") as file:
    content = file.read()

result = reverse_words(content)

with open(output_file, "w", encoding="utf-8") as file:
    file.write(result)

print("Готово")