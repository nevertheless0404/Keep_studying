# https://school.programmers.co.kr/learn/courses/30/lessons/92342


from itertools import combinations_with_replacement


def solution(n, score):
    result = [-1]
    max_cnt = -1

    # 중복 조합으로 0~10점까지 n개 뽑아보기!
    for i in combinations_with_replacement(range(11), n):
        # 라이언의 과녁 점수!!
        score2 = [0] * 11

        for j in i:
            # 라이언 과녁 점수에 넣기
            score2[10 - j] += 1

        apeach = 0
        lion = 0

        for k in range(11):
            # 둘 다 맞추지 않은 경우!
            if score[k] == score2[k] == 0:
                continue
            # 어피치가 라이언이 쏜 화살의 수 이상을 맞힌 경우
            # 어피치 점수
            elif score[k] >= score2[k]:
                apeach += 10 - k
            else:
                lion += 10 - k

        # 라이언이 점수가 더 높은 경우
        if lion > apeach:
            # 점수 차
            gap = lion - apeach
            # 기존보다 더 큰 점수 차이!
            if gap > max_cnt:
                max_cnt = gap
                result = score2
    return result
