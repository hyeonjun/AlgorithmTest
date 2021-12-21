for _ in range(int(input())):
    n, m = map(int, input().split())
    answer = 0
    for i in range(n, m+1):
        answer += str(i).count('0')
    print(answer)