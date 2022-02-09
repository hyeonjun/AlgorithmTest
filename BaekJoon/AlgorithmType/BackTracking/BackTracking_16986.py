from itertools import permutations
n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
P = [[0 for i in range(1, 21)]]
for _ in range(2):
    P.append(list(map(int, input().split())))

def check():
    idx = [0, 0, 0]
    win = [0, 0, 0]
    p1, p2, p3 = 0, 1, 2

    while True:
        if p1 > p2:
            p1, p2 = p2, p1 # p2가 경기 순서상 뒤
        # 지우가 낼 수 있는 손동작을 모두 다 쓰거나 다른 사람들이 손동작을 모두 다 냈을 경우
        if (p1 == 0 and idx[0] >= n) or idx[p1] >= 20 or idx[p2] >= 20:
            break
        # 플레이어 손 동작
        a, b = P[p1][idx[p1]], P[p2][idx[p2]]
        idx[p1] += 1
        idx[p2] += 1

        if arr[a-1][b-1] == 2:
            win[p1] += 1
            if win[p1] == k:
                break
            p2, p3 = p3, p2
        else:
            # 무승부 -> 뒤 사람이 이김
            win[p2] += 1
            if win[p2] == k:
                break
            p1, p3 = p3, p1
    return win[0] >= k

answer = 0
for p in permutations(range(1, n + 1)):
    for i in range(len(p)):
        P[0][i] = p[i]
    if check():
        answer = 1
        break
print(answer)