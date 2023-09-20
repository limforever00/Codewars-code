def likes(names):
    
    like = ' like this'
    likes = ' likes this'

    if(len(names) == 0):
        return 'no one' + likes
    elif(len(names) == 1):
        return names[0] + likes
    elif(len(names) == 2):
        return '{0} and {1}'.format(names[0], names[1]) + like
    elif(len(names) == 3):
        return '{0}, {1} and {2}'.format(names[0],names[1],names[2]) + like
    elif(len(names) > 3):
        others = len(names)-2
        return '{0}, {1} and {2} others'.format(names[0],names[1],others) + like
