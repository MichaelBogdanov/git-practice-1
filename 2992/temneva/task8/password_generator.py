# 8) Генератор пароля
# Цель: сгенерировать случайный пароль заданной длины с наборами символов
# Требования:
# Опции: включать/исключать цифры, прописные/строчные буквы, спецсимволы
# Обязательно минимум по одному символу из включённых наборов (если длина позволяет)

import random
import string

def generate_password(length=12, use_lower=True, use_upper=True, use_digits=True, use_special=True):
    chars = ""
    if use_lower: chars += string.ascii_lowercase
    if use_upper: chars += string.ascii_uppercase
    if use_digits: chars += string.digits
    if use_special: chars += "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    if not chars:
        return "Ошибка: не выбран ни один набор символов"
    if length < 4:
        return "Ошибка: минимальная длина пароля - 4 символа"
    
    # хотя бы по 1 символу из каждого набора
    password = []
    if use_lower: password.append(random.choice(string.ascii_lowercase))
    if use_upper: password.append(random.choice(string.ascii_uppercase))
    if use_digits: password.append(random.choice(string.digits))
    if use_special: password.append(random.choice("!@#$%^&*()_+-=[]{}|;:,.<>?"))
    
    selected_sets = sum([use_lower, use_upper, use_digits, use_special])
    if length < selected_sets:
        return f"Ошибка: длина пароля ({length}) меньше количества выбранных наборов ({selected_sets})"
    
    while len(password) < length:
        password.append(random.choice(chars))
    
    # перемешивание символов
    random.shuffle(password)
    return ''.join(password)

def get_valid_length():
    while True:
        try:
            length_input = input("Длина пароля (минимум 4): ").strip()
            if not length_input:
                length_input = "12"  # по умолчанию
            
            length = int(length_input)
            
            if length < 4:
                print("Ошибка: минимальная длина пароля - 4 символа. Попробуйте снова.")
                continue
                
            return length
        except ValueError:
            print("Ошибка: введите целое число для длины пароля. Попробуйте снова.")

def get_boolean_input(prompt):
    while True:
        value = input(prompt).strip().lower()
        if value in ['y', 'yes', 'да', '']:  # пустой ввод = согласие
            return True
        elif value in ['n', 'no', 'нет']:
            return False
        else:
            print("Ошибка: введите 'y' (да) или 'n' (нет). Попробуйте снова.")

def main():
    print("ГЕНЕРАТОР ПАРОЛЕЙ")
    print("=" * 40)
    
    while True:
        print("\n" + "=" * 40)
        print("НАСТРОЙКИ ПАРОЛЯ:")
        print("=" * 40)
        
        length = get_valid_length()
        
        print("\nВключать ли наборы символов (Enter = да):")
        use_lower = get_boolean_input("  • Строчные буквы (a-z) [y/n]: ")
        use_upper = get_boolean_input("  • Прописные буквы (A-Z) [y/n]: ")
        use_digits = get_boolean_input("  • Цифры (0-9) [y/n]: ")
        use_special = get_boolean_input("  • Спецсимволы (!@#$...) [y/n]: ")
        
        password = generate_password(length, use_lower, use_upper, use_digits, use_special)
        
        print("\n" + "=" * 40)
        print("РЕЗУЛЬТАТ:")
        print("=" * 40)
        
        if password.startswith("Ошибка"):
            print(password)
            print("\nПожалуйста, исправьте настройки и попробуйте снова.")
        else:
            print(f"Ваш пароль: {password}")
            print(f"Длина: {len(password)} символов")
            
            stats = {
                'lower': sum(1 for c in password if c.islower()),
                'upper': sum(1 for c in password if c.isupper()),
                'digits': sum(1 for c in password if c.isdigit()),
                'special': sum(1 for c in password if not c.isalnum())
            }
            
            print("\nСостав пароля:")
            if stats['lower'] > 0: print(f"  • Строчных букв: {stats['lower']}")
            if stats['upper'] > 0: print(f"  • Прописных букв: {stats['upper']}")
            if stats['digits'] > 0: print(f"  • Цифр: {stats['digits']}")
            if stats['special'] > 0: print(f"  • Спецсимволов: {stats['special']}")
        
        print("\n" + "=" * 40)
        print("1. Сгенерировать новый пароль")
        print("2. Выйти из программы")
        
        while True:
            choice = input("\nВыберите действие (1-2): ").strip()
            if choice == '1':
                break
            elif choice == '2':
                return
            else:
                print("Ошибка: введите 1 или 2.")

if __name__ == "__main__":
    main()