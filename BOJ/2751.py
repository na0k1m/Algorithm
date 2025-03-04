# Silver 5
# 수 정렬하기 2
# https://www.acmicpc.net/problem/2751

import sys

input = sys.stdin.readline
print = sys.stdout.write

num = int(input())
numList = []
a = 0

for i in range(num):
    a = int(input())
    numList.append(a)

numList.sort()

for a in numList:
    print(f"{a}\n")