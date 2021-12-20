prime = []
for i in range(2, 1000):
    flag = True
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            flag = False
    if flag:
        prime.append(i)

def check(x):
    for i in prime:
        for j in prime:
            for k in prime:
                if i+j+k == n:
                    print(i, j, k)
                    return
                if k > n:
                    continue
            if j > n:
                continue
        if i > n:
            continue
    print(0)

for _ in range(int(input())):
    n = int(input())
    check(n)