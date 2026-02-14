with open('input.txt', 'r', encoding='utf-8') as file:
    elements = file.read().split()

unique_elements = []
for item in elements:
    if item not in unique_elements:
        unique_elements.append(item)

with open('output.txt', 'w', encoding='utf-8') as file:
    file.write(' '.join(unique_elements))

print(f"Было элементов: {len(elements)}")
print(f"Стало элементов: {len(unique_elements)}")