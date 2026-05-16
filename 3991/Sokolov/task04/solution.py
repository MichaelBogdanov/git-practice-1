import sys

def delete_duplicates(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            items = content.split()
            
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 else 'git/git-practice-1/git-practice-1/3991/Sokolov/task04/text.txt'
    result = delete_duplicates(filename)
    if result:
        print(' '.join(result))