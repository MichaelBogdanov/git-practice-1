def check_brackets(text: str) -> str:
    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    opening = set(pairs.values())
    stack = []

    for char in text:
        if char in opening:
            stack.append(char)
        elif char in pairs:
            if not stack or stack[-1] != pairs[char]:
                return "NO"
            stack.pop()

    return "YES" if not stack else "NO"


if __name__ == "__main__":
    text = input("Введите строку: ")
    print(check_brackets(text))