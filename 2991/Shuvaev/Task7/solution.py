from collections import Counter


def char_frequency(filename: str, ignore_case: bool = False) -> dict:
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()

    if ignore_case:
        text = text.lower()

    counter = Counter(text)
    return dict(counter.most_common())


if __name__ == "__main__":
    file_url = input()
    #C:\\Users\\User\\Desktop\\test.txt пример
    freq = char_frequency(file_url, ignore_case=False)
    for ch, cnt in freq.items():
        print(f"'{ch}': {cnt}")