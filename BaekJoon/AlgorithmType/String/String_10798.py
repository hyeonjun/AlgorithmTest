strings = [input() for _ in range(5)]
answer = ''
for i in range(max(len(s) for s in strings)):
    for j in range(5):
        if i < len(strings[j]):
            answer += strings[j][i]
print(answer)