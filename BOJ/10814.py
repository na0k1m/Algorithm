# Silver 5
# 나이순 정렬
# https://www.acmicpc.net/problem/10814

n = int(input())
members = []

for i in range(n):
    age, name = input().split()
    members.append((int(age), i, name))

members.sort(key=lambda x: (x[0], x[1]))
# x[0] (나이) 에 따라 sort 하고 x[1] (가입순서) 에 따라 두번째 sort

for member in members:
    print(member[0], member[2])