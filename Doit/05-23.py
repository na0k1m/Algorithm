# Silver 5
# 연결 요소의 개수 구하기
# https://www.acmicpc.net/problem/11724

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

# 실행한 DFS의 실행 횟수 -> 연결 요소 개수
n, m = map(int, input().split())
g = [[] for _ in range(n+1)] # 리스트 안에 리스트
visited = [False for _ in range(n+1)]

def DFS(v):
    visited[v] = True
    for i in g[v]:
        if not visited[i]:
            DFS(i)


for i in range(m):
    s, e = map(int, input().split())
    g[s].append(e)
    g[e].append(s)

count = 0

for i in range(1, n+1):
    if not visited[i]:
        count += 1
        DFS(i)

print(count)