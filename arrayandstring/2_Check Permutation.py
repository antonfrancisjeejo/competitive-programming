string1 = input()
string2 = input()
new_string1 = sorted(string1)
new_string2 = sorted(string2)
flag = 0
if len(string1) != len(string2):
    print('Not a permutation of the string')
else:
    for i in range(len(string1)):
        if new_string1[i] != new_string2[i]:
            flag = 1
            break
    if flag == 0:
        print('Is a permutation of the string')
    else:
        print('Not a permutation of the string')
