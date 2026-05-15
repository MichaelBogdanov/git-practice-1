ip = input("Введите IP-адрес: ")

parts = ip.split(".")

is_correct = True

if len(parts) != 4:
    is_correct = False
else:
    for part in parts:

        if not part.isdigit():
            is_correct = False
            break

        number = int(part)

        if number < 0 or number > 255:
            is_correct = False
            break

if is_correct:
    print("IP-адрес корректный")
else:
    print("IP-адрес некорректный")