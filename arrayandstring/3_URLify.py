string = input().strip()
result = []
for letter in string:
    if letter == " ":
        result.append("%20")
    else:
        result.append(letter)
print("".join(result))
