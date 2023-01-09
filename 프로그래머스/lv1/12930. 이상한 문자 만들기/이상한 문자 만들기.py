def solution(s):
    answer = ''
    new = s.split(' ')
    for i in new:
        for j in range(len(i)):
            if j % 2 == 0:
                answer += i[j].upper()
            else:
                answer += i[j].lower()
        answer += ' '
        # 맨 마지막에 공백이 있어서 제외
    return answer[:-1]