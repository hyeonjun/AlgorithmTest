def solution(orders, course):
    answer = []
    # 가장 많이 함께 주문한 단품메뉴
    # 최소 2가지 이상의 메뉴 and 최소 2명 이상의 손님이 시킨거
    from itertools import combinations
    menu = {}
    for i in orders:
        for j in course:
            for c in combinations(i, j):
                data = ''.join(sorted(c))
                if data in menu:
                    menu[data] += 1
                else:
                    menu[data] = 1
    menu = sorted(menu.items(), key=lambda x: (len(x[0]), x[1]))
    menu = list(filter(lambda x: x[1] >= 2, menu)) # 개수가 1인 것들은 제외시켜버림
    maxC = menu[-1][1]
    length = course[-1]
    while menu:
        m, c = menu.pop()
        if len(m) == length and c >= maxC:
            answer.append(m)
        elif len(m) != length:
            maxC = c
            length = len(m)
            answer.append(m)

    return sorted(answer)

# ["AC", "ACDE", "BCFG", "CDE"]
# print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
# ["ACD", "AD", "ADE", "CD", "XYZ"]
# print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
# ["WX", "XY"]
# print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))

def solution(orders, course): # 시간상 위와 큰 차이는 없음
    from itertools import combinations
    from collections import Counter
    answer = []
    for i in course:
        candidates = []
        for m in orders:
            for c in combinations(m, i):
                tmp = ''.join(sorted(c))
                candidates.append(tmp)
        candidates = Counter(candidates).most_common() # Counter를 사용하면 딕셔너리에 넣고 개수를 올리고 정렬하는 것이 한번에 처리됨
        answer += [menu for menu, cnt in candidates if cnt > 1 and cnt == candidates[0][1]] # Counter는 내림차순
    return sorted(answer)

# ["AC", "ACDE", "BCFG", "CDE"]
print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
# ["ACD", "AD", "ADE", "CD", "XYZ"]
# print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
# ["WX", "XY"]
# print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))
















