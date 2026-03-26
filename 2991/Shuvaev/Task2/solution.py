import re

def count_lines_words_longest_word(filename: str) -> dict:
    lines = 0
    words = 0
    longest_word = ""
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            lines += 1
            words_in_line = re.split(r"[^\w'\-]+", line.strip())
            words_in_line = [w for w in words_in_line if w]
            words += len(words_in_line)
            for w in words_in_line:
                if len(w) > len(longest_word):
                    longest_word = w

    f.close()

    return {
        "lines": lines,
        "words": words,
        "longest_word": longest_word,
        "longest_len": len(longest_word),
    }


if __name__ == "__main__":
    file_url = input()
    #C:\\Users\\User\\Desktop\\test.txt  пример
    result = count_lines_words_longest_word(file_url)
    print("Lines:  ", result["lines"])
    print("Words:  ", result["words"])
    print("Longest word:", result["longest_word"])
    print("Length: ", result["longest_len"])


