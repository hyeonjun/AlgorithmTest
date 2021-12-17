string = input()
answer = []
for i in range(1, len(string)-1):
    for j in range(i+1, len(string)):
        a, b, c = string[:i][::-1], string[i:j][::-1], string[j:][::-1]
        answer.append(''.join(a+b+c))
print(sorted(answer)[0])