# Bronze 1
# 수 정렬하기
# https://www.acmicpc.net/problem/2750

import sys
input = sys.stdin.readline

n = int(input())
numList = []

for i in range(n):
    numList.append(int(input()))

for i in range(n-1):
    for j in range(n-1-i):
        if numList[j] > numList[j+1]:
            temp = numList[j]
            numList[j] = numList[j+1]
            numList[j+1] = temp

for i in range(n):
    print(numList[i])
