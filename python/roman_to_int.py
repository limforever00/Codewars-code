def solution(roman : str) -> int:
    """complete the solution by transforming the roman numeral into an integer"""

    roman_text = ['I','V','X','L','C','D','M']
    roman_val = [1,5,10,50,100,500,1000]

    arr = list(roman)

    res = 0

    for idx, val in enumerate(arr):
        if idx != 0:
            # 다음 idx가 없는지도 체크해야해!!
            if idx+1 == len(arr) or roman_text.index(val) >= roman_text.index(arr[idx+1]):
                print(1)
                res += roman_val[roman_text.index(val)]
            else :
                print(2)
                res -= roman_val[roman_text.index(val)]
        else :
            # 길이가 1인 배열이 올때도 체크해주기
            if idx+1 == len(arr) or roman_text.index(val) >= roman_text.index(arr[idx+1]):
                print(3)
                res += roman_val[roman_text.index(val)]
            else :
                print(4)
                res -= roman_val[roman_text.index(val)]   

        print(val)
        print(res)
        print('---------------------------------')
    return res


# print(solution('MMMCMXCIX'))

print(solution('MMMDCCCLXXXVIII'))
