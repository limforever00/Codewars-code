# Well met with Fibonacci bigger brother, AKA Tribonacci.

# As the name may already reveal, it works basically like a Fibonacci, but summing the last 3 (instead of 2) numbers of the sequence to generate the next. 
# And, worse part of it, regrettably I won't get to hear non-native Italian speakers trying to pronounce it :(

# So, if we are to start our Tribonacci sequence with [1, 1, 1] as a starting input (AKA signature), we have this sequence:

# [1, 1 ,1, 3, 5, 9, 17, 31, ...]
# But what if we started with [0, 0, 1] as a signature? As starting with [0, 1] instead of [1, 1] basically shifts the common Fibonacci sequence by once place, 
# you may be tempted to think that we would get the same sequence shifted by 2 places, but that is not the case and we would get:

# [0, 0, 1, 1, 2, 4, 7, 13, 24, ...]

def tribonacci(signature, n):
    # 배열의 요소를 더하지 않아도 될경우 
    # 있는거중에 뽑아서 리턴
    if n <= 3:
        arr = []
        for i in range(0,n):
            arr.append(signature[i])
            
        return arr

    # 배열의 요소를 추가해야 할 경우
    # 뒤에 3개를 더해서 append
    while len(signature) < n and n > 3:
        signature.append(signature[-1] + signature[-2] + signature[-3])

    # 일단 계산해놓고 n까지 리턴하는 경우
    # while len(signature) < n:
    #     signature.append(sum(signature[-3:]))
    
    # return signature[:n]    

    return signature    


