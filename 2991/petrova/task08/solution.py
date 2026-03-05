#!/usr/bin/env python3
"""
Задача 8: Генератор пароля
Генерирует случайный пароль с заданными параметрами
"""

import sys
import random
import string
import argparse

class PasswordGenerator:
    """Класс для генерации паролей"""
    
    # Наборы символов
    LOWERCASE = string.ascii_lowercase      # a-z
    UPPERCASE = string.ascii_uppercase      # A-Z
    DIGITS = string.digits                   # 0-9
    SPECIAL = "!@#$%^&*()_+-=[]{}|;:,.<>?"   # Спецсимволы
    
    def __init__(self):
        self.charsets = []      # Список выбранных наборов
        self.all_chars = ""     # Все доступные символы
        self.charset_names = [] # Названия наборов для вывода
    
    def configure(self, use_digits=True, use_lower=True, use_upper=True, use_special=True):
        """
        Настройка наборов символов для генерации
        
        Аргументы:
            use_digits: использовать цифры
            use_lower: использовать строчные буквы
            use_upper: использовать заглавные буквы
            use_special: использовать спецсимволы
        """
        self.charsets = []
        self.all_chars = ""
        self.charset_names = []
        
        if use_lower:
            self.charsets.append(self.LOWERCASE)
            self.all_chars += self.LOWERCASE
            self.charset_names.append("строчные")
        
        if use_upper:
            self.charsets.append(self.UPPERCASE)
            self.all_chars += self.UPPERCASE
            self.charset_names.append("ЗАГЛАВНЫЕ")
        
        if use_digits:
            self.charsets.append(self.DIGITS)
            self.all_chars += self.DIGITS
            self.charset_names.append("цифры")
        
        if use_special:
            self.charsets.append(self.SPECIAL)
            self.all_chars += self.SPECIAL
            self.charset_names.append("спецсимволы")
        
        if not self.charsets:
            raise ValueError("Должен быть выбран хотя бы один набор символов")
    
    def generate(self, length=8):
        """
        Генерирует пароль заданной длины
        
        Аргументы:
            length (int): длина пароля
            
        Возвращает:
            str: сгенерированный пароль
        """
        if length < len(self.charsets):
            raise ValueError(
                f"Длина пароля ({length}) меньше количества выбранных наборов ({len(self.charsets)}). "
                f"Нужно минимум {len(self.charsets)} символов, чтобы включить по одному из каждого набора."
            )
        
        password = []
        
        # Берем по одному символу из каждого набора
        for charset in self.charsets:
            password.append(random.choice(charset))
        
        # Заполняем оставшуюся длину случайными символами
        remaining = length - len(password)
        if remaining > 0:
            password.extend(random.choice(self.all_chars) for _ in range(remaining))
        
        # Перемешиваем, чтобы символы из наборов были в случайных местах
        random.shuffle(password)
        
        return ''.join(password)
    
    def get_password_strength(self, password):
        """
        Оценивает сложность пароля
        
        Возвращает: (оценка, описание)
        """
        score = 0
        feedback = []
        
        # Оценка длины
        if len(password) >= 12:
            score += 3
            feedback.append("✓ Отличная длина")
        elif len(password) >= 8:
            score += 2
            feedback.append("✓ Хорошая длина")
        else:
            score += 1
            feedback.append(" Маленькая длина")
        
        # Проверка наличия разных типов символов
        has_lower = any(c.islower() for c in password)
        has_upper = any(c.isupper() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(c in self.SPECIAL for c in password)
        
        types_count = sum([has_lower, has_upper, has_digit, has_special])
        score += types_count
        
        if has_lower and has_upper:
            feedback.append("✓ Есть буквы разного регистра")
        if has_digit:
            feedback.append("✓ Есть цифры")
        if has_special:
            feedback.append("✓ Есть спецсимволы")
        
        # Разнообразие символов
        unique_ratio = len(set(password)) / len(password)
        if unique_ratio > 0.7:
            score += 2
            feedback.append("✓ Высокое разнообразие символов")
        elif unique_ratio > 0.5:
            score += 1
            feedback.append("✓ Среднее разнообразие")
        
        # Оценка
        if score >= 8:
            strength = " СЛОЖНЫЙ"
        elif score >= 5:
            strength = " СРЕДНИЙ"
        else:
            strength = "️ ПРОСТОЙ"
        
        return strength, feedback

def main():
    parser = argparse.ArgumentParser(
        description="Генератор безопасных паролей",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Примеры использования:
  python solution.py                    # пароль 8 символов (все наборы)
  python solution.py -l 12               # пароль 12 символов
  python solution.py -n 5                 # 5 паролей
  python solution.py --no-special         # без спецсимволов
  python solution.py --only-digits        # только цифры
  python solution.py -l 16 -n 3 --no-special  # комбинация
  python solution.py --check MyP@ss       # проверить пароль
        """
    )
    
    parser.add_argument('-l', '--length', type=int, default=8,
                       help='длина пароля (по умолчанию: 8)')
    parser.add_argument('-n', '--count', type=int, default=1,
                       help='количество паролей (по умолчанию: 1)')
    parser.add_argument('--no-digits', action='store_true',
                       help='без цифр')
    parser.add_argument('--no-lower', action='store_true',
                       help='без строчных букв')
    parser.add_argument('--no-upper', action='store_true',
                       help='без заглавных букв')
    parser.add_argument('--no-special', action='store_true',
                       help='без спецсимволов')
    parser.add_argument('--only-digits', action='store_true',
                       help='только цифры')
    parser.add_argument('--only-letters', action='store_true',
                       help='только буквы (строчные и заглавные)')
    parser.add_argument('--check', metavar='ПАРОЛЬ',
                       help='проверить сложность пароля')
    
    args = parser.parse_args()
    
    # Режим проверки пароля
    if args.check:
        generator = PasswordGenerator()
        generator.configure(use_digits=True, use_lower=True, 
                          use_upper=True, use_special=True)
        
        password = args.check
        strength, feedback = generator.get_password_strength(password)
        
        print("\n" + "=" * 50)
        print(" АНАЛИЗ ПАРОЛЯ")
        print("=" * 50)
        print(f"Пароль: {password}")
        print(f"Длина: {len(password)} символов")
        print(f"Сложность: {strength}")
        print("\nДетальный анализ:")
        for item in feedback:
            print(f"  {item}")
        return
    
    # Режим генерации
    try:
        generator = PasswordGenerator()
        
        # Определяем наборы символов
        if args.only_digits:
            use_digits, use_lower, use_upper, use_special = True, False, False, False
        elif args.only_letters:
            use_digits, use_lower, use_upper, use_special = False, True, True, False
        else:
            use_digits = not args.no_digits
            use_lower = not args.no_lower
            use_upper = not args.no_upper
            use_special = not args.no_special
        
        generator.configure(use_digits, use_lower, use_upper, use_special)
        
        # Показываем настройки
        print("\n" + "=" * 60)
        print(" ГЕНЕРАТОР ПАРОЛЕЙ")
        print("=" * 60)
        print(f" Длина: {args.length} символов")
        print(f" Количество: {args.count}")
        print(f" Наборы: {', '.join(generator.charset_names)}")
        print("-" * 60)
        
        # Генерируем пароли
        for i in range(args.count):
            try:
                password = generator.generate(args.length)
                strength, _ = generator.get_password_strength(password)
                print(f"{i+1:2}. {password:20} {strength}")
            except ValueError as e:
                print(f" Ошибка: {e}")
                return
        
        print("=" * 60)
        
    except ValueError as e:
        print(f" Ошибка: {e}")
        return

def demo():
    """Демонстрация работы генератора"""
    print("=" * 60)
    print("ДЕМОНСТРАЦИЯ ГЕНЕРАТОРА ПАРОЛЕЙ")
    print("=" * 60)
    
    generator = PasswordGenerator()
    
    # Тест 1: Стандартный пароль
    generator.configure(True, True, True, True)
    print("\n1. Стандартный пароль (все наборы):")
    for i in range(3):
        pwd = generator.generate(10)
        strength, _ = generator.get_password_strength(pwd)
        print(f"   {pwd} - {strength}")
    
    # Тест 2: Только буквы
    generator.configure(False, True, True, False)
    print("\n2. Только буквы:")
    for i in range(3):
        pwd = generator.generate(8)
        strength, _ = generator.get_password_strength(pwd)
        print(f"   {pwd} - {strength}")
    
    # Тест 3: Только цифры
    generator.configure(True, False, False, False)
    print("\n3. Только цифры:")
    for i in range(3):
        pwd = generator.generate(6)
        strength, _ = generator.get_password_strength(pwd)
        print(f"   {pwd} - {strength}")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--demo":
        demo()
    else:
        main()