n = int(input())
string = [input() for _ in range(n)]
answer = ''
flag = False
for i in string:
    for j in string:
        if i == j[::-1]:
            answer = i
            break
    if flag:
        break
print(len(answer), answer[len(answer)//2])