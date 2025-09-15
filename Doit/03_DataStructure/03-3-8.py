# Gold 5
# 좋다
# https://www.acmicpc.net/problem/1253

import sys
input = sys.stdin.readline

n = int(input())
numList = list(map(int, input().split()))
numList.sort()
count = 0

for k in range(n):
    find = numList[k]
    i, j = 0, n - 1
    while i < j:
        if numList[i] + numList[j] == find:
            if i != k and j != k:
                count += 1
                break
            elif i == k:
                i += 1
            elif j == k:
                j -= 1
        elif numList[i] + numList[j] > find:
            j -= 1
        elif numList[i] + numList[j] < find:
            i += 1

print(count)