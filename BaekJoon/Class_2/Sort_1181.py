n = int(input())
words = []
for _ in range(n):
    words.append(input())
for i in sorted(set(words), key=lambda x:(len(x), x)):
    print(i)
