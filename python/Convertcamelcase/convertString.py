# Complete the method/function so that it converts dash/underscore delimited words into camel casing. 
# The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). 
# The next words should be always capitalized.

def to_camel_case(text):

    list2 = []
    res = ''

    for val in list(text):
        if (ord(val) >= 65 and ord(val) <= 90) or (ord(val) >=97 and ord(val) <=123):
            list2.append(val)
        else :
            list2.append('up')
    

    for idx,li in enumerate(list2):
        if(li == 'up'):
            list2[idx+1] = list2[idx+1].upper()
        else:
            res += li

    return res

text = "the-stealth-warrior"
print(to_camel_case(text))