from itertools import permutations
def solution(user_id, banned_id):
    answer = []

    def check(ban, can):
        for i in range(len(ban)):
            if len(ban[i]) != len(can[i]):
                return False
            for j in range(len(ban[i])):
                if ban[i][j] == '*':
                    continue
                if ban[i][j] != can[i][j]:
                    return False
        return True

    for candidate_id in permutations(user_id, len(banned_id)):
        if check(banned_id, candidate_id):
            candidate_id = set(candidate_id)
            if candidate_id not in answer:
                answer.append(candidate_id)

    return len(answer)

user_id = [
["frodo", "fradi", "crodo", "abc123", "frodoc"],
["frodo", "fradi", "crodo", "abc123", "frodoc"],
["frodo", "fradi", "crodo", "abc123", "frodoc"]
]

banned_id = [
["fr*d*", "abc1**"],
["*rodo", "*rodo", "******"],
["fr*d*", "*rodo", "******", "******"]
]

for u,b in zip(user_id, banned_id):
    print(solution(u, b))
# 2
# 2
# 3