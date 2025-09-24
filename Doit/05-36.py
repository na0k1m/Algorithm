# Silver 2
# 잃어버린 괄호(최솟값을 만드는 괄호 배치 찾기)
# https://www.acmicpc.net/problem/1541

import sys
input = sys.stdin.readline

problem = list(map(str, input().split("-")))
answer = 0

def mySum(i):
    sum = 0
    temp = list(map(int, i.split("+")))
    for i in temp:
        sum += i
    return sum

for i in range(len(problem)):
    temp = mySum(problem[i])
    if i == 0:
        answer += temp
    else:
        answer -= temp

print(answer)