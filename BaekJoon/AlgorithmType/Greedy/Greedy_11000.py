import heapq
n = int(input())
st = [list(map(int, input().split())) for _ in range(n)]
st.sort()

room = []
heapq.heappush(room, st[0][1])

for i in range(1, n):
    if st[i][0] < room[0]:
        heapq.heappush(room, st[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, st[i][1])
print(len(room))