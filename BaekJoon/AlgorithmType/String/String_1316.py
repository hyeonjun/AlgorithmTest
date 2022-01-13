answer = 0
for _ in range(int(input())):
    string = input()
    flag = True
    for i in range(len(string)-1):
        if string[i] != string[i+1]:
            if string[i+1:].count(string[i]) > 0:
               flag = False
               break
    if flag:
        answer += 1
print(answer)