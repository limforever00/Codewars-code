# A pangram is a sentence that contains every single letter of the alphabet at least once. 
# For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

# Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

def is_pangram(str):
    chk = list('abcdefghijklmnopqrstuvwxyz')

    li = list(str.lower())

    for i in li:
        if i in chk:
            chk.remove(i)

    if len(chk) == 0:        
        return True
    else:
        return False


a = is_pangram('The quick brown fox jumps over the lazy dog') # True
b = is_pangram('1bcdefghijklmnopqrstuvwxyz') # False

if is_pangram(a) == True:
    print('정답')
else :
    print('오답')

if is_pangram(b) == False:
    print('정답')
else :
    print('오답')

