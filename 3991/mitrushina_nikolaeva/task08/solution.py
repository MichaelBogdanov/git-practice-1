import random
import string

def generate_password(length, use_digits=True, use_lower=True, use_upper=True, use_special=True):
    digits = string.digits  
    lower = string.ascii_lowercase  
    upper = string.ascii_uppercase  
    special = "!@#$%^&*()_-+=<>?/[]{}|"
    
    #все разрешенные символы
    all_chars = ""
    required_sets = []
    
    if use_digits:
        all_chars += digits
        required_sets.append(digits)
    if use_lower:
        all_chars += lower
        required_sets.append(lower)
    if use_upper:
        all_chars += upper
        required_sets.append(upper)
    if use_special:
        all_chars += special
        required_sets.append(special)
    #выбераем множество символов
    if not all_chars:
        return "Ошибка: нужно выбрать набор символов"
    if length < len(required_sets):
        return f"Ошибка: длина пароля должна быть не меньше {len(required_sets)} (количество выбранных наборов)"
    password = []
    #добавляем по одному символу из каждого набора
    for chars in required_sets:
        password.append(random.choice(chars))
    #заполняем случайными символами
    for _ in range(length - len(required_sets)):
        password.append(random.choice(all_chars))
    random.shuffle(password)
    return ''.join(password)

def simple_password_generator():    
    try:
        length = int(input("Введите длину пароля: "))
        if length <= 0:
            print("Длина должна быть положительным числом")
            return
    except ValueError:
        print("Ошибка: введите целое число")
        return
    
    print("\nВыберите наборы символов (да/нет):")
    use_digits = input("Включить цифры? (да/нет): ").lower() in ['да', 'yes', 'y', 'д']
    use_lower = input("Включить строчные буквы? (да/нет): ").lower() in ['да', 'yes', 'y', 'д']
    use_upper = input("Включить прописные буквы? (да/нет): ").lower() in ['да', 'yes', 'y', 'д']
    use_special = input("Включить спецсимволы? (да/нет): ").lower() in ['да', 'yes', 'y', 'д']
    
    password = generate_password(length, use_digits, use_lower, use_upper, use_special)
    print(f"Сгенерированный пароль: {password}")


if __name__ == "__main__":
    print("Пароль длиной 8 со всеми наборами")
    print(generate_password(8))
       