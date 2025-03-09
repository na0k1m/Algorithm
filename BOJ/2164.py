# Silver 4
# 카드2
# https://www.acmicpc.net/problem/2164

# 1 버려
# 2
# 3
# 4
# 젤 위꺼 버리고 그담 젤 위꺼 맨 아래로

import sys
from collections import deque

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
cardQueue = deque(range(1, n + 1))

while len(cardQueue) > 1:
    cardQueue.popleft()
    cardQueue.append(cardQueue.popleft())

print(f"{cardQueue[0]}\n")

# n = int(input())
# cardList = []

# for i in range(1, n + 1):
#     cardList.append(i)

# while (len(cardList) != 1):
#     del cardList[0]
#     cardList.append(cardList[0])
#     del cardList[0]

# print(cardList[0])