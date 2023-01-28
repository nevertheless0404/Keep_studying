def solution(numbers):
    stack = []
    answer = [0] * len(numbers)
    
    # 뒤에 있는 큰수가 없는 인덱스가 남도록 함 
    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)
    
    # 뒤에 큰수가 없는 경우 인덱스 자리에 -1로 넣음 
    while stack:
        answer[stack.pop()] = -1
    
    return answer
