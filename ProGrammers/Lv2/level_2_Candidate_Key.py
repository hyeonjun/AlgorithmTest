def solution(relation):
    from itertools import combinations
    row = len(relation)
    col = len(relation[0])

    candidates = []
    for i in range(1, col + 1):
        for j in combinations(range(col), i):
            candidates.append(j)

    unique = []
    for idx in candidates:
        tmp = [tuple(data[i] for i in idx) for data in relation]
        if len(set(tmp)) == row:
            unique.append(idx)

    # 	{(0, 1), (1, 2), (0, 1, 2), (0, 1, 3), (0, 3), (0, 2, 3), (1, 2, 3), (0, 2), (0, 1, 2, 3), (0,)}

    answer = set(unique[:])
    for i in range(len(unique)):
        for j in range(i + 1, len(unique)):
            # print(unique[i], unique[j], set(unique[i]) & set(unique[j]))
            if len(unique[i]) == len(set(unique[i]) & set(unique[j])):  # intersection -> tuple은 & 사용 불가
                # if len(unique[i]) == len(set(unique[i]).intersection(set(unique[j]))):
                answer.discard(unique[j])

    return len(answer)

relation = [["100","ryan","music","2"],
            ["200","apeach","math","2"],
            ["300","tube","computer","3"],
            ["400","con","computer","4"],
            ["500","muzi","music","3"],
            ["600","apeach","music","2"]]
print(solution(relation)) # 2

