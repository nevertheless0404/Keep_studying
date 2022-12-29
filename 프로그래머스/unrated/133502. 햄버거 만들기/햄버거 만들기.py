def solution(ingredient):
    ham = []
    cnt = 0
    for i in ingredient:
        ham.append(i)
        if ham[-4:] == [1, 2, 3, 1]:
            cnt += 1
            for j in range(4):
                ham.pop()
    return cnt