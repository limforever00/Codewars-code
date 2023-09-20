# Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

# Examples:
# Input: 42145 Output: 54421

# Input: 145263 Output: 654321

# Input: 123456789 Output: 987654321

num = 52893

# if type(num) is int:
#     numList = list(map(int, str(num))).sort(reverse=True)
#     ret =''
#     for i in numList:
#        ret += str(i)

#     print(ret)


if type(num) is int:
    if(num > 0):
        # numList = list(map(int, str(num)))
        # numList.sort(reverse=True)
        # print(type(numList))
        # str = sorted(numList,reverse=True)
        # print(str.join())
        str = "".join(sorted(str(num),reverse=True))
        print(str)
        print(type(str))
        str2 = "".join(str)
        print(str2)
        # ret =''
        # for i in numList:
        #     ret += str(i)

        #     print(int(ret))
    

# def Descending_Order(num):
#     return int("".join(sorted(str(num), reverse=True)))    

# print(Descending_Order(num));