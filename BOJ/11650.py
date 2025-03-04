# Silver 5
# 좌표 정렬하기
# https://www.acmicpc.net/problem/11650

n = int(input())
coordinates = []

for i in range(n):
    x, y = input().split()
    coordinates.append((int(x), int(y)))

coordinates.sort(key=lambda x: (x[0], x[1]))

for coordinate in coordinates:
    print(coordinate[0], coordinate[1])