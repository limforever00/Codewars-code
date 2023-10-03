# Write a function named first_non_repeating_letter that takes a string input, and returns the first character that is not repeated anywhere in the string.

# For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in the string, and occurs first in the string.

# As an added challenge, upper- and lowercase letters are considered the same character, but the function should return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.

# If a string contains all repeating characters, it should return an empty string ("") or None -- see sample tests.


# 이 문제를 해결하기 위한 방법을 아래에 간략하게 설명해 드리겠습니다:

# 대소문자 구분 없이 처리: 문자열을 순회하기 전에 모든 문자를 소문자로 변환한 복사본을 만듭니다. 이렇게 하면 대소문자 구분 없이 문자의 빈도를 계산할 수 있습니다.

# 빈도 계산: 문자열의 각 문자에 대한 빈도를 계산합니다. 이를 위해 딕셔너리를 사용할 수 있습니다. 딕셔너리의 키는 문자이고 값은 해당 문자의 빈도입니다.

# 첫 번째 비반복 문자 찾기: 원래 문자열을 처음부터 순회하면서 해당 문자의 빈도가 1인지 확인합니다. 빈도가 1인 첫 번째 문자를 반환합니다. 모든 문자가 반복되면 빈 문자열이나 None을 반환합니다.

# 이 방법을 사용하면 주어진 문자열을 두 번만 순회하면 됩니다. 첫 번째 순회는 빈도를 계산하기 위한 것이고, 두 번째 순회는 첫 번째 비반복 문자를 찾기 위한 것입니다.

# 이제 이 방법을 코드로 구현하면 됩니다!

def first_non_repeating_letter(s):
    if len(s) == 0:
        return ''
    
    sCopy = s.lower()

    sDic = {}
    # 각 문자에 대한 빈도 계산해서 dic에 저장
    for i in list(sCopy):
        # if sDic.get(i) is None:
        #     sDic[i] = sCopy.count(i)
        # 시간복잡도가 O(n^2)이므로 한번만 순회하게 수정
        sDic[i] = sDic.get(i, 0) + 1

    # 복사본에서 반복이1인 문자열의 index를 확인하고 원본에서 해당 인덱스 리턴
    for idx, val in enumerate(list(sCopy)):
        if sDic[val] == 1:
            return s[idx]

    return ''


a = first_non_repeating_letter('abcda')
print(a)