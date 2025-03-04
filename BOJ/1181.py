# Silver 5
# 단어 정렬
# https://www.acmicpc.net/problem/1181

num = int(input())
wordList = []

for i in range(num):
    word = input()
    if word not in wordList:
        wordList.append(word)

wordList = sorted(wordList, key=lambda x: (len(x), x))

for word in wordList:
    print(word)