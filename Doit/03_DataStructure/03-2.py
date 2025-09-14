# Silver 3
# 구간 합 구하기 4
# https://www.acmicpc.net/problem/11659

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numList = list(map(int, input().split()))
sumList = [0]
temp = 0

for i in numList:
    temp = temp + i
    sumList.append(temp)

for i in range(m):
    a, b = map(int, input().split())
    print(sumList[b] - sumList[a-1])
