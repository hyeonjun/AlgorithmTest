triangle = [n * (n+1) // 2 for n in range(1, 45)]
for _ in range(int(input())):
    n = int(input())
    flag = False
    for i in triangle:
        for j in triangle:
            for k in triangle:
                if i + j + k == n:
                    flag = True
    print(1 if flag else 0)