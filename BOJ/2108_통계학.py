# https://www.acmicpc.net/problem/2108

import sys
input = sys.stdin.readline

n = int(input())
nums = []
num_dict = {}

for _ in range(n):
    num = int(input())
    nums.append(num)
    if num not in num_dict:
        num_dict[num] = 1
    else:
        num_dict[num] += 1

print(round(sum(nums)/n))

nums.sort()
print(nums[n//2])

max_= max(num_dict.values())
temp = []
for key, value in num_dict.items():
    if value == max_:
        temp.append(key)

temp.sort()
if len(temp) != 1:
    print(temp[1])
else:
    print(temp[0])

print(nums[-1] - nums[0])


# import sys

# input = sys.stdin.readline

# n = int(input())
# nums = sorted([int(input()) for _ in range(n)])
# num = [[0] * 2 for _ in range(4001)]

# print(round(sum(nums) / n)) #산술 평균
# print(nums[n//2])# 중앙값

# for i in nums:
#     # 마이너스, 플러스 구분
#     if i < 0:
#         num[abs(i)][0] += 1 #마이너스 라면 이중리스트에서의 해당 숫자 인덱스로 접근 그리구 그중 앞에부분을[0] +1
#     else:
#         num[i][1] += 1 # 반대로 플러스면 [1] +1

# mx_0 = 0 # 마이너스부분중 맥스값 찾기 위한 변수
# mx_1 = 0 # 플러스 부분중 맥스값 찾기 위한 변수

# # 0~ 4001 까지 맥스 값 찾자
# for i in range(4001):
#     mx_0 = max(mx_0, num[i][0])
#     mx_1 = max(mx_1, num[i][1])

# # 그중 마이너스최댓값 와 플러스최댓값 중 큰 값
# mx_mix = max(mx_0, mx_1)
# c = []

# for i in range(4001):
#     # 마이너스 부분
#     if num[i][0] == mx_mix and num[i][0]:
#         c.append(-i)
#     # 플러스 부분
#     if num[i][1] == mx_mix and num[i][1]:
#         c.append(i)
# # 정렬
# c.sort()
# # 한개라면 첫번째
# if len(c) == 1:
#     print(c[0])
# # 두개이상 이라면 두번째꺼
# else:
#     print(c[1])
# # 범위
# print(nums[-1] - nums[0])