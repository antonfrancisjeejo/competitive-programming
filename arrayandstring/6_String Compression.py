def string_compress(word):
    result = []
    value = 0
    for i in range(len(word) - 1):
        key = word[i]
        if key == word[i + 1]:
            value += 1
        else:
            result.append(key)
            result.append(value + 1)
            value = 0
    result.append(key)
    result.append(value + 1)
    return result


word = input()
compressed_string = string_compress(word)
if len(word) < len(compressed_string):
    print(word)
else:
    print(*compressed_string, sep='')
