def rle_code(s):
    if not s:
        return ""
    result = ""
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result += s[i - 1] + str(count)
            count = 1

    result += s[-1] + str(count)
    return result
def rle_decode(d):
    result = ""
    count = ""

    for char in d:
        if char.isdigit():
            count += char
        else:
            if count:
                result += prev_char * int(count)
            prev_char = char
            count = ""

    result += prev_char * int(count)
    return result
s = input()
d = input()
encoded = rle_code(s)
decoded = rle_decode(d)

print(encoded) 
print(decoded)
