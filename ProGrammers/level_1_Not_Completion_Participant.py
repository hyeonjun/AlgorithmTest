def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    N = len(participant)
    try:
        for i in range(N):
            if participant[i] != completion[i]:
                answer = participant[i]
                break
    except:
        answer = participant[-1]

    return answer

print(solution(["marina", "josipa", "nikola", "vinko", "filipa"],["josipa", "filipa", "marina", "nikola"]))
# print(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))