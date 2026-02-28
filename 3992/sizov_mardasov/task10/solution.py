# Задача 10 — Проверка IP-адреса
# Определяет: IPv4, IPv6 или INVALID
# Бонус: нормализует IPv6 (убирает лишние нули)


def check_ipv4(address):
    """
    Проверяет, является ли строка корректным IPv4.
    Формат: 4 числа от 0 до 255, разделённые точкой.
    """
    parts = address.split(".")

    # Должно быть ровно 4 части
    if len(parts) != 4:
        return False

    for part in parts:
        # Часть не должна быть пустой
        if not part:
            return False
        # Недопустимы ведущие нули (01, 001 и т.д.), кроме "0"
        if len(part) > 1 and part[0] == "0":
            return False
        # Только цифры
        if not part.isdigit():
            return False
        # Значение от 0 до 255
        if not (0 <= int(part) <= 255):
            return False

    return True


def check_ipv6(address):
    """
    Проверяет, является ли строка корректным IPv6.
    Формат: 8 групп из 1–4 шестнадцатеричных цифр, разделённых двоеточием.
    """
    parts = address.split(":")

    # Должно быть ровно 8 групп
    if len(parts) != 8:
        return False

    hex_chars = set("0123456789abcdefABCDEF")

    for part in parts:
        # Каждая группа от 1 до 4 символов
        if not (1 <= len(part) <= 4):
            return False
        # Только шестнадцатеричные символы
        if not all(c in hex_chars for c in part):
            return False

    return True


def normalize_ipv6(address):
    """
    Нормализует IPv6: убирает ведущие нули в каждой группе.
    Пример: 2001:0db8:0000:0000:0000:0000:0000:0001
         -> 2001:db8:0:0:0:0:0:1
    """
    parts = address.split(":")
    # Убираем ведущие нули в каждой группе, но оставляем хотя бы "0"
    normalized = [part.lstrip("0") or "0" for part in parts]
    return ":".join(normalized)


def validate_ip(address):
    """Основная функция: возвращает 'IPv4', 'IPv6' или 'INVALID'."""
    address = address.strip()

    if check_ipv4(address):
        return "IPv4"

    if check_ipv6(address):
        normalized = normalize_ipv6(address)
        return f"IPv6 (нормализованный: {normalized})"

    return "INVALID"


# --- Запуск ---
if __name__ == "__main__":
    print("Проверка IP-адреса")
    print("Введите адрес (или 'стоп' для выхода):\n")

    while True:
        user_input = input("IP: ").strip()
        if user_input.lower() in ("стоп", "stop", "exit", "quit"):
            break
        result = validate_ip(user_input)
        print(f"  Результат: {result}\n")
