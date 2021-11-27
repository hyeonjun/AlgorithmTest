for _ in range(int(input())):
    n = int(input())
    candidate = [list(map(int, input().split())) for _ in range(n)]
    candidate.sort()
    minV = candidate[0][1]
    answer = 1
    for i in range(1, n):
        if minV > candidate[i][1]:
            minV = candidate[i][1]
            answer += 1
    print(answer)