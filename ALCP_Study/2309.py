# bronze 1
# 일곱 난쟁이
# https://www.acmicpc.net/problem/2309

heightList = []
heightSum = 0
found = False

for i in range(9):
    height = int(input())
    heightList.append(height)
    heightSum += height

for i in range(8):
    for j in range(i+1, 9):
        if heightSum - heightList[i] - heightList[j] == 100:
            result = [heightList[k] for k in range(9) if k != i and k != j]
            result.sort()
            for height in result:
                print(height)
            found = True
            break
    if found == True:
        break