n = int(input())
if n < 100:
    print(n)
else:
    answer = 99
    for i in range(100, n+1):
        num = list(map(int, str(i)))
        if num[0] - num[1] == num[1] - num[2]:
            answer += 1
    print(answer)