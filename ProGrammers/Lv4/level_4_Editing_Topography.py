def solution(land, P, Q):
    # P는 추가비용, Q는 제거비용
    lst = []
    for i in land:
        lst += i
    lst.sort()

    n = len(lst)
    answer = sum(lst) * Q  # 0층으로 맞출때의 비용
    cost = (sum(lst) - lst[0] * n) * Q  # 최소 높이로 만드는 비용
    answer = min(answer, cost)

    for i in range(1, n):
        if lst[i] != lst[i - 1]:
            cost += (P * i * (lst[i] - lst[i - 1])) - (Q * (n - i) * (lst[i] - lst[i - 1]))
            answer = min(answer, cost)

print(solution([[1, 2], [2, 3]], 3, 2)) # 5
print(solution([[4, 4, 3], [3, 2, 2], [ 2, 1, 0 ]], 5, 3)) # 33