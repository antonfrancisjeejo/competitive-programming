no_of_chars = 128


def palindrome(word):
    count = [0] * no_of_chars
    for i in range(len(word)):
        count[ord(word[i])] = count[ord(word[i])] + 1
    flag = 0
    for i in range(no_of_chars):
        if count[i] & 1:
            flag += 1
        if flag > 1:
            return False
    return True


word = input()
if palindrome(word):
    print('Is a palindrome permutation')
else:
    print('Not a palindrome permutation')
