def one_away(string1, string2):
    str1_length = len(string1)
    str2_length = len(string2)
    if str1_length == str2_length:
        if string1 == string2:
            return True
        
        else:
            difference = 0
            for i in range(str1_length):
                if string1[i] != string2[i]:
                    difference += 1
            return difference == 1
    elif abs(str1_length - str2_length) == 1:
        small_string = string1 if (str1_length < str2_length) else string2
        long_string = string1 if (str1_length > str2_length) else string2
        change = 0
        for i in range(len(small_string)):
            if small_string[i] != long_string[i + change]:
                if change:
                    return False
                change = 1
        return True
    else:
        return False


string1 = input()
string2 = input()
if one_away(string1, string2):
    print('One away')
else:
    print('Not one away')
