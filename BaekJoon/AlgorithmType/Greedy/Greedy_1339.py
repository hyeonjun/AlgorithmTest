n = int(input())
words = [input() for _ in range(n)]
dic = {}
for word in words:
    length = len(word)
    for w in word:
        if w not in dic:
            dic[w] = (10 ** (length-1))
        else:
            dic[w] += (10 ** (length-1))
        length -= 1

value = sorted(dic.values(), reverse=True)
num = 9
answer = 0
for i in value:
    answer += i * num
    num -= 1
print(answer)