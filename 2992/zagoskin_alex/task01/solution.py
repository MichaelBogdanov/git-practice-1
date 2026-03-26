def check_brackets(text: str) -> str:
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []

    for char in text:
        if char in "([{":
            stack.append(char)
        elif char in pairs:
            if not stack or stack[-1] != pairs[char]:
                return "NO"
            stack.pop()

    return "YES" if not stack else "NO"


if __name__ == "__main__":
    s = input()
    print(check_brackets(s))