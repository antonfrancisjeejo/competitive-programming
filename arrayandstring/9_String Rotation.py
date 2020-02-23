def issubstring(string1, string2):
    true = 0
    if len(string1) != len(string2):
        return False
    for i in range(len(string2)):
        x = string1[0:i]
        y = string1[i:]
        if (y + x) == string2:
            true = 1
        if true:
            return True
        else:
            continue
    if not true:
        return False


string1 = input()
string2 = input()
if issubstring(string1, string2):
    print("Yes it is it's rotation")
else:
    print("No it is not it's rotation")
