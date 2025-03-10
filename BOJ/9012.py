# Silver 4
# 괄호
# https://www.acmicpc.net/problem/9012

t = int(input())

for i in range(t):
    parenthesisString = input()
    parenthesisStack = []
    for j in parenthesisString:
        if j == "(":
            parenthesisStack.append(j)
        elif j == ")":
            if parenthesisStack: # 스택 비어있지 않으면
                parenthesisStack.pop()
            else: # 스택 비어있으면
                print("NO")
                break
    else:
        if not parenthesisStack:
            print("YES")
        else:
            print("NO")