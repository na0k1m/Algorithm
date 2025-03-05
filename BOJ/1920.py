# Silver 4
# 수 찾기
# https://www.acmicpc.net/problem/1920

import sys

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
nSet = set(map(int, input().split()))

m = int(input())
mList = map(int, input().split())

for num in mList:
    if num in nSet:
        print("1\n")
    else:
        print("0\n")