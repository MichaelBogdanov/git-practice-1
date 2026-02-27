import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from solution import validate_ip, normalize_ipv6

# IPv4
assert validate_ip("192.168.1.1") == "IPv4"
assert validate_ip("0.0.0.0") == "IPv4"
assert validate_ip("255.255.255.255") == "IPv4"

# Невалидный IPv4
assert validate_ip("256.0.0.1") == "INVALID"
assert validate_ip("192.168.1") == "INVALID"
assert validate_ip("01.02.03.04") == "INVALID"  # ведущие нули

# IPv6
result = validate_ip("2001:0db8:0000:0000:0000:0000:0000:0001")
assert result.startswith("IPv6")

# Нормализация IPv6
assert normalize_ipv6("2001:0db8:0000:0000:0000:0000:0000:0001") == "2001:db8:0:0:0:0:0:1"

# Невалидный
assert validate_ip("not_an_ip") == "INVALID"
assert validate_ip("::1") == "INVALID"  # сокращённая нотация не поддерживается

print("Все тесты пройдены!")
