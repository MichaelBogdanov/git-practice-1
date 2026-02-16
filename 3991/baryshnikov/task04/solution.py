import sys


if __name__ == "__main__":
    with open(sys.argv[1], 'r') as file:
        numbers = list(map(int, " ".join(file.readlines()).split()))
        res = []
        for n in numbers:
            if not n in res:
                res.append(n)
    
    with open(sys.argv[1], 'w') as file:
        print(" ".join(list(map(str, res))), file=file)
        
        