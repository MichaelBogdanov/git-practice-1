# Задача 8: Генератор пароля

import random
import string

def generate_password(length, use_uppercase=True, use_lowercase=True, 
                      use_digits=True, use_special=True):
    
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    available = []
    required = []
    
    if use_uppercase:
        available.extend(uppercase)
        required.append(random.choice(uppercase))
    if use_lowercase:
        available.extend(lowercase)
        required.append(random.choice(lowercase))
    if use_digits:
        available.extend(digits)
        required.append(random.choice(digits))
    if use_special:
        available.extend(special)
        required.append(random.choice(special))
    
    if not available:
        return "Ошибка: нужно выбрать хотя бы один тип символов"
    
    if length < len(required):
        return f"Ошибка: длина пароля ({length}) меньше требуемого минимума ({len(required)})"
    
    remaining = length - len(required)
    for _ in range(remaining):
        required.append(random.choice(available))
    
    random.shuffle(required)
    
    return ''.join(required)

print("=" * 50)
print("Задача 8: Генератор пароля")
print("=" * 50)

print("Настройки генератора:")

try:
    length = int(input("Длина пароля: "))
    use_upper = input("Включать заглавные буквы? (да/нет): ").lower() in ['да', 'yes', 'y', 'д']
    use_lower = input("Включать строчные буквы? (да/нет): ").lower() in ['да', 'yes', 'y', 'д']
    use_digits = input("Включать цифры? (да/нет): ").lower() in ['да', 'yes', 'y', 'д']
    use_special = input("Включать спецсимволы? (да/нет): ").lower() in ['да', 'yes', 'y', 'д']
    
    password = generate_password(length, use_upper, use_lower, use_digits, use_special)
    
    print(f"\nСгенерированный пароль: {password}")
    
    print("\nЕщё 3 варианта пароля:")
    for i in range(3):
        p = generate_password(length, use_upper, use_lower, use_digits, use_special)
        print(f"{i+1}. {p}")
        
except ValueError:
    print("Ошибка: длина должна быть числом")