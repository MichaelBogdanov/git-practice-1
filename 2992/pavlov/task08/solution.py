import random
import string

def get_yes_no_input(prompt):
    """Функция для получения ответа да/нет от пользователя"""
    while True:
        response = input(prompt + " (y/n): ").lower()
        if response in ['y', 'yes']:
            return True
        elif response in ['n', 'no']:
            return False
        else:
            print("Пожалуйста, введите 'y' или 'n'")

def generate_password(length, use_digits, use_lower, use_upper, use_special):
    """Генерация пароля с заданными параметрами"""
    
    char_sets = [] # Определяем наборы символов
    required_chars = []
    
    if use_digits:
        char_sets.append(string.digits)
        required_chars.append(random.choice(string.digits))
    
    if use_lower:
        char_sets.append(string.ascii_lowercase)
        required_chars.append(random.choice(string.ascii_lowercase))
    
    if use_upper:
        char_sets.append(string.ascii_uppercase)
        required_chars.append(random.choice(string.ascii_uppercase))
    
    if use_special:
        special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        char_sets.append(special_chars)
        required_chars.append(random.choice(special_chars))
    
    if not char_sets:
        print("Ошибка: необходимо выбрать хотя бы один набор символов!")
        return None

    if length < len(required_chars):
        print(f"Ошибка: минимальная длина пароля для выбранных опций - {len(required_chars)} символов")
        return None
    
    all_chars = ''.join(char_sets)
    password = required_chars.copy()
    
    # Добавляем случайные символы до нужной длины
    for _ in range(length - len(required_chars)):
        password.append(random.choice(all_chars))
    
    # Перемешиваем символы
    random.shuffle(password)
    return ''.join(password)

def main():
    print("ГЕНЕРАТОР ПАРОЛЕЙ")
    print()
    
    # Запрос длины пароля
    while True:
        try:
            length = int(input("Введите длину пароля: "))
            if length < 1:
                print("Длина должна быть положительным числом!")
                continue
            break
        except ValueError:
            print("Введите целое число!")
    
    print("\nВыберите наборы символов для пароля:")
    use_digits = get_yes_no_input("Включать цифры (0-9)")
    use_lower = get_yes_no_input("Включать строчные буквы (a-z)")
    use_upper = get_yes_no_input("Включать прописные буквы (A-Z)")
    use_special = get_yes_no_input("Включать специальные символы (!@#$...)")
    
    # Генерация пароля
    print("\n" + "="*40)
    password = generate_password(length, use_digits, use_lower, use_upper, use_special)
    
    if password:
        print(f"Сгенерированный пароль: {password}")
        print(f"Длина пароля: {len(password)} символов")
        
        score = sum([use_digits, use_lower, use_upper, use_special])
        if length >= 12 and score >= 3:
            print("Надежность: Высокая ✓")
        elif length >= 8 and score >= 2:
            print("Надежность: Средняя")
        else:
            print("Надежность: Низкая")

if __name__ == "__main__":
    main()