string = input()
flag = 0
for letter in string:
    if string.count(letter) > 1:
        flag = 1
        break
    else:
        flag = 0
if flag == 0:
    print('All Unique')
else:
    print('Not Unique')

