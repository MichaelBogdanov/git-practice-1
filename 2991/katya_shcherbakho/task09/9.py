def rle_encode(s: str) -> str:
    if not s:
        return ""
    encoded = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            encoded.append(s[i-1] + str(count))
            count = 1
    encoded.append(s[-1] + str(count))
    return ''.join(encoded)

def rle_decode(s: str) -> str:
    decoded = []
    i = 0
    while i < len(s):
        ch = s[i]
        i += 1
        num_str = ''
        while i < len(s) and s[i].isdigit():
            num_str += s[i]
            i += 1
        if num_str:
            count = int(num_str)
        else:
            count = 1   
        decoded.append(ch * count)
    return ''.join(decoded)

if __name__ == "__main__":
    test_str = "AAABBBCCDAA"
    encoded = rle_encode(test_str)
    decoded = rle_decode(encoded)
    print(f"Исходная: {test_str}")
    print(f"Закодированная: {encoded}")   # A3B3C2D1A2
    print(f"Декодированная: {decoded}")