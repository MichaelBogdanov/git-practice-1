import sys

def check_brackets(s: str) -> str:
    #1 задание проверяет правильность расстановки скобок () [] {}

    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for ch in s:
        if ch in '([{':
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack[-1] != pairs[ch]:
                return "NO"
            stack.pop()
    return "YES" if not stack else "NO"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
    input_str = sys.argv[1]
    print(check_brackets(input_str))