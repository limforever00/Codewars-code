# You are given an array (which will have a length of at least 3, but could be very large) containing integers. 
# The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. 
# Write a method that takes the array as an argument and returns this "outlier" N.

# Examples
# [2, 4, 0, 100, 4, 11, 2602, 36]
# Should return: 11 (the only odd number)

# [160, 3, 1719, 19, 11, 13, -21]
# Should return: 160 (the only even number)

def find_outlier(integers):

    # 반복문 한번만 돌아서 하는방법
    # 한번돌때 리스트2개에 각각 추가해서 len이 1인 배열의 값만 리턴
    #oddList = []
    # evenList = []
    
    # for i in integers:
    #     if i % 2 == 0 :
    #         evenList.append(i)
    #     else :
    #         oddList.append(i)
    
    # if len(evenList) == 1:
    #     return evenList[0]
    # else :
    #     return oddList[0]

    resStr = 'even'
    cntOdd = 0
    cntEven = 0

    # 짝수 홀수중 적은건 하나만 있기때문에 원소중 앞에 3개만 체크해도 찾아야할거를 알수있음
    for i in range(0,3):
        if integers[i] % 2 == 0: 
            cntEven+=1     
        else: 
            cntOdd+=1

    if(cntOdd > cntEven):
        resStr = 'odd'
    else:
        pass

    for i in integers:
        if resStr == 'even':
            if i%2 != 0:
                return i
        else:
            if i%2 == 0:
                return i
            
list = [2, 4, 6, 8, 10, 3]
print(find_outlier(list))

list = [160, 3, 1719, 19, 11, 13, -21]
print(find_outlier(list))
