def solution(n):
    answer = 0
    # 에라토스테네스 체
    # 검증할 숫자를 담을 배열 
    ch = [0] * (n+1)
    for i in range(2, n+1):
        if ch[i] == 0:
            answer += 1
            # 소수라고 판단했던 수의 배수들을 전부 1로 !
            for j in range(i, n+1 , i):
                ch[j] = 1
    return answer
    # for n in range(2, n+1):
    #     for i in range(2, n):
    #         if n%i == 0:
    #             break
    #     else:
    #         answer += 1
    # return answer