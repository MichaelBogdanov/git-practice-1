import sys

def check_brackets(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for ch in s:
        if ch in '([{':
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return "NO"
    return "YES" if not stack else "NO"

if __name__ == "__main__":
    line = sys.stdin.readline().strip()
    print(check_brackets(line))