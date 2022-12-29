def solution(arr):
    answer = []
    if len(arr) == 1:
        answer.append(-1)
    else:
        answer = arr
        answer.remove(min(arr))
    return answer