# Silver 4
# 수 찾기
# https://www.acmicpc.net/problem/1920

import sys
input = sys.stdin.readline

n = int(input())
nList = list(map(int, input().split()))
nList.sort()

m = int(input())
mList = list(map(int, input().split()))

for i in range(m):
    find = False
    start = 0
    end = n-1
    while start <= end:
        midi = (start+end) // 2
        if mList[i] < nList[midi]:
            end = midi - 1
        elif mList[i] > nList[midi]:
            start = midi + 1
        else:
            find = True
            break
    if find:
        print(1)
    else:
        print(0)