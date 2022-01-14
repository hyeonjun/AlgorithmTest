n = int(input())
A = list(input())
answer = 0
for _ in range(n-1):
    Y = list(input())
    X = A[:]
    for _ in range(len(Y)):
        y = Y.pop(0)
        if y in X:
            X.remove(y)
        else:
            Y.append(y)
    a, b = len(X), len(Y)
    if ((a == 0 or a == 1) and (b == 0 or b == 1)):
        answer += 1
print(answer)