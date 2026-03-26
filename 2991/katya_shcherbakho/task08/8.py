import random
import string

def generate_password(length: int, use_digits: bool, use_lower: bool, use_upper: bool, use_special: bool) -> str:

    if length < 1:
        return ""


    char_sets = []
    if use_digits:
        char_sets.append(string.digits)
    if use_lower:
        char_sets.append(string.ascii_lowercase)
    if use_upper:
        char_sets.append(string.ascii_uppercase)
    if use_special:
        char_sets.append(string.punctuation)

    if not char_sets:
        return ""


    mandatory = []
    for cs in char_sets:
        mandatory.append(random.choice(cs))

    if len(mandatory) > length:

        mandatory = mandatory[:length]


    all_chars = ''.join(char_sets)
    remaining = length - len(mandatory)
    rest = [random.choice(all_chars) for _ in range(remaining)]
    password_list = mandatory + rest
    random.shuffle(password_list)   # перемешиваем
    return ''.join(password_list)

if __name__ == "__main__":
    print(generate_password(12, True, True, True, True))