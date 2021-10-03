for _ in range(int(input())):
    n = int(input())
    costume = {}
    for _ in range(n):
        a, b = input().split()
        if b not in costume:
            costume[b] = 1
        else:
            costume[b] += 1
    result = 1
    for i in costume:
        result *= costume[i] + 1
    print(result-1)

"""
(의상 종류의 개수 +1) * (의상 종류의 개수 +1) * .. -1
"""