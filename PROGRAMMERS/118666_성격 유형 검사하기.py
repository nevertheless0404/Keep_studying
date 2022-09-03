# https://school.programmers.co.kr/learn/courses/30/lessons/118666

def solution(survey, choices):
    answer = ''
    check = {"R":0, "T":0, "C":0, "F":0, "J":0, "M":0, "A":0, "N":0, }
    for i in range(len(choices)):
        l = survey[i][0]
        r = survey[i][1]
        if choices[i] == 4:
            continue
        elif choices[i] < 4:
            check[l] += (4 - choices[i])
        else:
            check[r] += (choices[i] - 4)
    answer += "R" if check["R"] >= check["T"] else "T"
    answer += "C" if check["C"] >= check["F"] else "F"
    answer += "J" if check["J"] >= check["M"] else "M"
    answer += "A" if check["A"] >= check["N"] else "N"
    return answer