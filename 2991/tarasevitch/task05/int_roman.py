def num_valid_rom(num):
    allowed = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    for n in num:
        if n not in allowed:
            return False
    return True

def num_valid_int(num):
    try:
        nums = int(num)
        if (nums > 3999 or nums < 1):
            return False
        return True
    except ValueError:
        return False

def roman_to_int(num):
    values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    total = 0

    for i in range(len(num)):
        if (i + 1 >= len(num)):
            total = total + values[num[i]]
            break
        if (values[num[i]] < values[num[i + 1]]):
            total = total - values[num[i]]
        else:
            total = total + values[num[i]]

    if (total > 3999):
        print("Значение не должно быть больше 3999!")
        return 0
    return total

def int_to_roman(num):
    values = [
        (1000, "M"),
        (900,  "CM"),
        (500,  "D"),
        (400,  "CD"),
        (100,  "C"),
        (90,   "XC"),
        (50,   "L"),
        (40,   "XL"),
        (10,   "X"),
        (9,    "IX"),
        (5,    "V"),
        (4,    "IV"),
        (1,    "I"),
    ]

    result = []

    for value, symbol in values:
        while num >= value:
            result.append(symbol)
            num -= value

        if num == 0:
            break

    return "".join(result)

print("Введите римское число (вплоть до 3999):")
while True:
    num = input()
    if(num_valid_rom(num)):
        print(roman_to_int(num))
    elif (num_valid_int(num)):
        nums = int(num)
        print(int_to_roman(nums))

    else:
        print("Неккоректный ввод!")