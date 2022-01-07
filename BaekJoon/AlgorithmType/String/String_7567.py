string = input()
answer = 10
for i in range(1, len(string)):
    if string[i] == string[i-1]:
        answer += 5
    else:
        answer += 10
print(answer)