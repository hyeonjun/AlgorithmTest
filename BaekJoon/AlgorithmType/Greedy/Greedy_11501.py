for _ in range(int(input())):
    n = int(input())
    stock = list(map(int, input().split()))
    answer = 0
    maxV = stock[-1]
    for i in range(n-1, -1, -1):
        if stock[i] > maxV:
            maxV = stock[i]
        else:
            answer += maxV - stock[i]
    print(answer)