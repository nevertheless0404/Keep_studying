def solution(n, arr1, arr2):
    answer = []
    
    for i, j in zip(arr1, arr2):
        # bin 10진수를 2진수로!
        t = str(bin(i | j)[2:])
        # rjust 전체자리 숫자, 공백이 있을 경우 공백 대체 문자 
        t = t.rjust(n, '0')
        t = t.replace('1', '#')
        t = t.replace('0', ' ')
        answer.append(t)
    return answer