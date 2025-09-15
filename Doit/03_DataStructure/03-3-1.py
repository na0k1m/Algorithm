# Silver 5
# 수들의 합 5
# https://www.acmicpc.net/problem/11659

import sys
input = sys.stdin.readline

n = int(input())
start_index, end_index = 1, 1
sum = 1
count = 1

while end_index != n:
    if sum < n:
        end_index += 1
        sum += end_index        
    elif sum > n:
        sum -= start_index
        start_index += 1
    elif sum == n:
        count += 1
        sum -= start_index
        start_index += 1
print(count)