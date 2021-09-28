n, k = map(int, input().split())
queue = [i for i in range(1, n+1)]
print("<", end='')
while queue:
    for i in range(k-1):
        queue.append(queue.pop(0))
    print(queue.pop(0), end='')
    if queue:
        print(", ", end='')
print(">")

""""
1 2 3 4 5 6 7
4 5 6 7 1 2 -> 3
7 1 2 4 5 -> 6
4 5 7 1 -> 2
1 4 5 -> 7
1 4 -> 5
4 -> 1
-> 4
출력 3 6 2 7 5 1 4
"""