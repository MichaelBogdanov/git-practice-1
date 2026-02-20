text = ""
with open("test.txt", "r") as file:
    text = file.read()
    file.close()

toLower = input("Учитывать регистр? (1 - да, 2 - нет)\n")
if toLower == "2":
    text = text.lower()

setText = set(text)
hashTabl = {}

for i in setText:
    hashTabl[i] = text.count(i)

print(sorted(hashTabl.items(), key=lambda x: x[1], reverse=True))



