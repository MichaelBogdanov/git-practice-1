a, b, c = map(int, input().split())
print("Трегольник", ("существует" if a + b > c and a + c > b and c + b > a else "не существует"))