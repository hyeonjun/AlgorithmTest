t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    priority = list(map(int, input().split()))
    queue = [[i,v] for i,v in enumerate(priority)]
    order = 0
    while queue:
        idx, prior = queue.pop(0)
        if len(queue) > 0 and prior < max(q[1] for q in queue):
            queue.append([idx, prior])
        else:
            order += 1
            if idx == m:
                print(order)
                break

"""
3
1 0
5
4 2
1 2 3 4
6 0
1 1 9 1 1 1
=> 1 2 5
"""