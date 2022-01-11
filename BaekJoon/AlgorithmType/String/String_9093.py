for _ in range(int(input())):
    string = input().split()
    answer = []
    for s in string:
        answer.append(s[::-1])
    print(*answer)