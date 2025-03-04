# Silver 4
# 체스판 다시 칠하기
# https://www.acmicpc.net/source/90840519

n, m = map(int, input().split())
matrix = []
count = []

for i in range(n):
    matrix.append(input())

for a in range(n - 7):
    for b in range(m - 7):
        wIndex = 0
        bIndex = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i + j) % 2 == 0:
                    if matrix[i][j] != 'W':
                        wIndex += 1
                    if matrix[i][j] != 'B':
                        bIndex += 1
                else:
                    if matrix[i][j] != 'B':
                        wIndex += 1
                    if matrix[i][j] != 'W':
                        bIndex += 1
        count.append(min(wIndex, bIndex))

print(min(count))