# Silver 4
# 숫자 카드 2
# https://www.acmicpc.net/problem/10816

import sys
input = sys.stdin.readline

n = input()
cardList = list(map(int, input().split()))
m = input()
toCheckList = list(map(int, input().split()))

cardCounts = {}
for c in cardList:
    if c in cardCounts:
        cardCounts[c] += 1
    else:
        cardCounts[c] = 1

answer = []
for t in toCheckList:
    if t in cardCounts:
        answer.append(cardCounts[t])
    else:
        answer.append(0)
print(*answer)