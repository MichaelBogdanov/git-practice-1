def correct_open_close(s):
    st = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for ch in s:
        if ch in '([{':
            st.append(ch)
        elif ch in ')]}':
            if not st or st.pop() != pairs[ch]:
                return False
    return not st

s = input()
print("YES" if correct_open_close(s) else "NO")
