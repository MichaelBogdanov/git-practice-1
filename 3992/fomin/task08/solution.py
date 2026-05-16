import random
import string

def generate_password(length: int, use_digits=True, use_lowercase=True, use_uppercase=True, use_special=True) -> str:
    if length <= 0:
        raise ValueError("Длина пароля должна быть больше 0")
    
    pool = ""
    password = []
    
    if use_digits and len(password) < length:
        password.append(random.choice(string.digits))
        pool += string.digits
    if use_lowercase and len(password) < length:
        password.append(random.choice(string.ascii_lowercase))
        pool += string.ascii_lowercase
    if use_uppercase and len(password) < length:
        password.append(random.choice(string.ascii_uppercase))
        pool += string.ascii_uppercase
    if use_special and len(password) < length:
        special_chars = "!@#$%^&*()-_=+[]{}|;:',.<>?/"
        password.append(random.choice(special_chars))
        pool += special_chars
        
    if not pool:
        raise ValueError("Должен быть выбран хотя бы один набор символов")
        
    while len(password) < length:
        password.append(random.choice(pool))
        
    random.shuffle(password)
    return "".join(password)

if __name__ == "__main__":
    try:
        length_input = input("Введите желаемую длину пароля: ")
        length = int(length_input)
        
        print("\nНастройте наборы символов (введите 'n' для отказа, или просто Enter для согласия):")
        ans_digits = input("Включать цифры? [Y/n]: ").strip().lower() != 'n'
        ans_lower = input("Включать строчные буквы? [Y/n]: ").strip().lower() != 'n'
        ans_upper = input("Включать прописные буквы? [Y/n]: ").strip().lower() != 'n'
        ans_special = input("Включать спецсимволы? [Y/n]: ").strip().lower() != 'n'
        
        pwd = generate_password(
            length, 
            use_digits=ans_digits, 
            use_lowercase=ans_lower, 
            use_uppercase=ans_upper, 
            use_special=ans_special
        )
        print(f"\nВаш сгенерированный пароль:\n{pwd}")
        
    except ValueError as e:
        print(f"Ошибка ввода: {e}")