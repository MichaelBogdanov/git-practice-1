input = ""
arr = []
result = True

try:
  for char in input:
    if char == ")":
      if arr[len(arr)-1] == "(":
        arr.pop(len(arr)-1)
      else:
        result = False
        break

    elif char == "}":
      if arr[len(arr)-1] == "{":
        arr.pop(len(arr)-1)
      else:
        result = False
        break

    elif char == "]":
      if arr[len(arr)-1] == "[":
        arr.pop(len(arr)-1)
      else:
        result = False
        break

    else:
      if (char == "(" or char == "[" or char == "{"):
        arr.append(char)
      
except IndexError:
  result = False


if (len(arr) != 0):
  result = False

print(result)