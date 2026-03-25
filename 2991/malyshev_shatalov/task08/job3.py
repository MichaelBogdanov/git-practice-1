import random
import string
import sys

def generate_password(length, use_digits, use_upper, use_lower, use_special):
    charset = []
    mandatory = []

    if use_digits:
        charset.extend(string.digits)
        mandatory.append(random.choice(string.digits))
    if use_lower:
        charset.extend(string.ascii_lowercase)
        mandatory.append(random.choice(string.ascii_lowercase))
    if use_upper:
        charset.extend(string.ascii_uppercase)
        mandatory.append(random.choice(string.ascii_uppercase))
    if use_special:
        charset.extend(string.punctuation)
        mandatory.append(random.choice(string.punctuation))

    if len(mandatory) > length:
        return "Ошибка: слишком короткая длина"

    password_list = mandatory[:]
    remaining_length = length - len(mandatory)
    charset_str = ''.join(set(charset))

    password_list.extend(random.choices(charset_str, k=remaining_length))
    random.shuffle(password_list)

    return ''.join(password_list)

if name == "main":
    if len(sys.argv) < 2:
        sys.exit(1)

    length = int(sys.argv[1])
    opts = {arg: True for arg in sys.argv[2:] if arg.startswith('-')}

    pwd = generate_password(
        length,
        opts.get('-d', False),
        opts.get('-U', False),
        opts.get('-l', False),
        opts.get('-s', False)
    )
    print(pwd)