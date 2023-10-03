# Implement a function that receives two IPv4 addresses, and returns the number of addresses between them (including the first one, excluding the last one).

# All inputs will be valid IPv4 addresses in the form of strings. The last address will always be greater than the first one.

def ips_between(start, end):
    startArr = start.split('.')
    endArr = end.split('.')

    sum = int(endArr[-1]) - int(startArr[-1])
    print('시작값 : ' , sum)

    for i in range(len(startArr)-2 , -1, -1):
        print(i)
        print('start : ',startArr[i])
        print('end : ',endArr[i])

        print('값 : ', int(endArr[i]) - int(startArr[i])) * (256**(3-i))

        sum += (int(endArr[i]) - int(startArr[i])) * (256**(3-i))
        print('sum : ',sum)

    return sum


ips_between("236.48.240.182","255.255.255.255")