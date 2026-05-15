# Задача 1: Проверка корректности скобок
# Поддерживаются: (), [], {}

def check_brackets(text):
    stack = []
    brackets = {')': '(', ']': '[', '}': '{'}
    
    for char in text:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack:
                return False
            if stack[-1] != brackets[char]:
                return False
            stack.pop()
    
    return len(stack) == 0

# Тестирование
print("=" * 50)
print("Задача 1: Проверка корректности скобок")
print("=" * 50)

tests = ["()", "()[]{}", "(]", "([)]", "{[]}", "((()))", "(()", "hello (world)"]

for test in tests:
    result = check_brackets(test)
    print(f"'{test}' -> {'YES' if result else 'NO'}")

# Интерактивный режим
print("\nИнтерактивный режим (введите 'exit' для выхода)")
while True:
    user_input = input("Введите строку: ")
    if user_input.lower() == 'exit':
        break
    result = check_brackets(user_input)
    print(f"Результат: {'YES' if result else 'NO'}")



if __name__ == "__main__":
    exit(main())