def solution(quiz):
    answer = []
    
    for i in quiz:
        n = i.split("=")
        for j in range(len(n)):
            if eval(n[0]) == eval(n[len(n)-1]):
                answer.append("O")
                break
            else:
                answer.append("X")
                break
    return answer



# exp = "1 + 2"
# result = eval(exp)
# print(result)
# 3