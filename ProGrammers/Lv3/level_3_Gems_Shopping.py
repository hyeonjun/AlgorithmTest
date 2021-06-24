def solution(gems):
    answer = [0, len(gems) - 1]
    dic = {gems[0]: 1}
    gems_set = len(set(gems))
    start, end = 0, 0

    while start <= end and end < len(gems):
        if len(dic) == gems_set:
            if end - start < answer[1] - answer[0]:
                answer = [start, end]
            if dic[gems[start]] == 1:
                del dic[gems[start]]
            else:
                dic[gems[start]] -= 1
            start += 1
        else:
            end += 1
            if end == len(gems):
                break
            if gems[end] not in dic:
                dic[gems[end]] = 1
            else:
                dic[gems[end]] += 1
    return [answer[0] + 1, answer[1] + 1]

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])) # [3, 7]
print(solution(["AA", "AB", "AC", "AA", "AC"])) # [1, 3]
print(solution(["XYZ", "XYZ", "XYZ"])) # [1, 1]
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"])) # [1, 5]