from itertools import combinations

def solution(nums):
    answer = 0
    cmb = list(combinations(nums, 3))
    for i in cmb:
        s = sum(i)
        result = True
        for i in range(2, int(s**0.5) + 1):
            if s%i == 0:
                result = False
        if result:
            answer +=1
    return answer