# Bronze 1
# 부녀회장이 될테야
# https://www.acmicpc.net/problem/2775

t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())
    floor0 = [x for x in range(1, n+1)]
    for i in range(k):
        for j in range(1, n):
            floor0[j] += floor0[j-1]
    print(floor0[-1])

# 0-1 1
# 0-2 2

# 1-1 1
# 1-2 1+2 = 3
# 1-3 1+2+3 = 6

# 2-1 1
# 2-2: 1 + (1+2) = 4
# 2-3: 1 + (1+2) + (1+2+3) = 10

# 3-3: 1 + (1+(1+2)) + (1+(1+2)+(1+2+3))