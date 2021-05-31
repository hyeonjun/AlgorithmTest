def solution(skill, skill_trees):
    answer = len(skill_trees)
    skill = list(skill)
    for i in skill_trees:
        tmp = [j for j in i if j in skill]
        for x, y in zip(skill, tmp):
            if x != y:
                answer -= 1
                break

    return answer

print("CBD", ["BACDE", "CBADF", "AECB", "BDA"]) # 2