# Silver 4
# 체스판 다시 칠하기
# https://www.acmicpc.net/source/90840519

n, m = map(int, input().split())
matrix = []
count = []

for i in range(n):
    matrix.append(input())

# 체스판 자르기
for a in range(n - 7):
    for b in range(m - 7):
        # 무슨 색으로 시작하는지 판별하기 위함
        wIndex = 0
        bIndex = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i + j) % 2 == 0: # 짝수 좌표
                    if matrix[i][j] != 'W':
                        wIndex += 1 # 'W' 가 아니라면 색칠
                    if matrix[i][j] != 'B':
                        bIndex += 1 # 'B' 가 아니라면 색칠
                else: # 홀수 좌표
                    if matrix[i][j] != 'B':
                        wIndex += 1
                    if matrix[i][j] != 'W':
                        bIndex += 1
        count.append(min(wIndex, bIndex))

print(min(count))