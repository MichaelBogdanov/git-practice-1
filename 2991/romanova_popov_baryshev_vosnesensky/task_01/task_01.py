# 1, 4, 6, 7, 8, 10 

def func():
    str = input()
    strStack = []

    for i in str:
        if i == "(" or i == "[" or i == "{":
            strStack += i

        elif i == ")" or i == "]" or i == "}":
            if(len(strStack) == 0):
                return "false"
            elif (i == ")" and strStack[-1] == "(") or (i == "]" and strStack[-1] == "[") or (i == "}" and strStack[-1] == "{"):
                strStack.pop()
        
    if(len(strStack) == 0):
        return "true"
    else:
        return "false"

print(func())
