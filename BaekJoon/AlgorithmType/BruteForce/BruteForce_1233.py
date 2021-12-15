s1, s2, s3 = map(int, input().split())
sumV = [0 for _ in range(81)]
for i in range(1, s1+1):
    for j in range(1, s2+1):
        for k in range(1, s3+1):
            sumV[i+j+k] += 1
print(sumV.index(max(sumV)))