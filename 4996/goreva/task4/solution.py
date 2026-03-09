def delete(file_path):
    file = open(file_path, 'r', encoding='utf-8')
    str = file.read()
    file.close()
    
    res = []

    for i in str.split(' '):
        if i not in res:
            res.append(i)
    return res

print(delete('file.txt'))