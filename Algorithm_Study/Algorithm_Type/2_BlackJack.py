def solution(N, M, Card):
    from itertools import combinations # 중복 불가능
    # from itertools import permutations # 중복 가능
    answer = [sum(i) for i in combinations(Card, 3) if sum(i) <= M]
    return max(answer)

print(solution(5, 21, [5,6,7,8,9]))
print(solution(10,500,[93, 181, 245, 214, 315, 36, 185, 138, 216, 295]))

def solution(N, M, Card):
    answer = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                tmp = Card[i]+Card[j]+Card[k]
                if tmp <= M:
                    answer = max(answer, tmp)
    return answer
    pass

print(solution(5, 21, [5,6,7,8,9]))
print(solution(10,500,[93, 181, 245, 214, 315, 36, 185, 138, 216, 295]))