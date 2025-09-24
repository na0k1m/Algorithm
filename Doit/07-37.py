# Silver 3
# 소수 구하기
# https://www.acmicpc.net/problem/1929

import math
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
primeNum = [0] * (n+1)

for i in range(2, n+1):
    primeNum[i] = i

for i in range(2, int(math.sqrt(n))+1):
    if primeNum[i] == 0:
        continue
    for j in range(i+i, n+1, i):
        primeNum[j] = 0

for i in range(m, n+1):
    if primeNum[i] != 0:
        print(primeNum[i])