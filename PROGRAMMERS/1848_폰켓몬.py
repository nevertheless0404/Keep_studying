# https://school.programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    answer = 0
    length = len(nums) // 2
    temp = list(set(nums))
    
    for value in temp :
        if(answer < length):
            answer +=1
            
    return answer