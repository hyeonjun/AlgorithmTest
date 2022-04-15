answer = []
for _ in range(int(input())):
    string = input()
    num = []
    for i in range(len(string)):
        if string[i].isdigit():
            num.append(string[i])
        else:
            if num:
                answer.append(int(''.join(num)))
                num.clear()
    if num:
        answer.append(int(''.join(num)))
for a in sorted(answer):
    print(a)