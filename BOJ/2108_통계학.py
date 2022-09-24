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


