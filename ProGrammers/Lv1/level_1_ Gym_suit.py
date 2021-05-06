def solution(n, lost, reserve):
    dif_reserve = [x for x in reserve if x not in lost]
    dif_lost = [x for x in lost if x not in reserve]


    for i in dif_reserve:
        if i - 1 in dif_lost:
            dif_lost.remove(i - 1)
        elif i + 1 in dif_lost:
            dif_lost.remove(i + 1)
    answer = n - len(dif_lost)
    return answer

# print(solution(5,[2,4],[1,3,5]))
# print(solution(5,[2,4],[3]))
print(solution(3,[3],[1]))