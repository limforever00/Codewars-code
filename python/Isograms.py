# An isogram is a word that has no repeating letters, consecutive or non-consecutive. 
# Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

# Example: (Input --> Output)

# "Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case)

# isIsogram "Dermatoglyphics" = true
# isIsogram "moose" = false
# isIsogram "aba" = false

def is_isogram(str):

    strArr = list(str.lower())

    for val in strArr:
        if strArr.count(val) > 1:  
            return False

    return True        

    # set 중복제거 되니까 이렇게 하는 사람도 많은거같다..
    #return len(str) == len(set(str.lower()))
    

print(is_isogram('myEyxp'))