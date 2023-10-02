#  Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

# HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59
# The maximum time never exceeds 359999 (99:59:59)

# You can find some examples in the test fixtures.

import math as m

def make_readable(seconds):

    hour = str(seconds // 3600)
    min = str((seconds % 3600)//60)
    sec = str(seconds % 60)

    if len(hour) == 1 :
        hour = '0' + hour

    if len(min) == 1 :
        min = '0' + min
    
    if len(sec) == 1 :
        sec = '0' + sec
    
    return hour + ":" + min + ":" + sec


a = make_readable(0)

print(a)
