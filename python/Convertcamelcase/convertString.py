# Complete the method/function so that it converts dash/underscore delimited words into camel casing. 
# The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). 
# The next words should be always capitalized.

def to_camel_case(text):

    valList = []
    res = ''

    for val in list(text):
        if ('A' <= val <= 'Z') or ('a' <= val <= 'z'):
            valList.append(val)
        else :
            valList.append('up')
    
    for idx,li in enumerate(valList):
        if li == 'up':
            if idx + 1 < len(valList):  # 다음 글자가 있는지 확인
                valList[idx+1] = valList[idx+1].upper()
        else:
            res += li

    return res

text = "the-stealth-warrior"
print(to_camel_case(text))