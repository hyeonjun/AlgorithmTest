def solution(msg):
    answer = []
    dictionary = {chr(65+i):i+1 for i in range(26)}
    s,e = 0,0
    while True:
        e += 1
        if msg[s:e+1] not in dictionary:
            dictionary[msg[s:e+1]] = len(dictionary)+1
            answer.append(dictionary[msg[s:e]])
            s = e
        if e == len(msg):
            answer.append(dictionary[msg[s:e]])
            break
    return answer

print(solution("KAKAO")) # [11, 1, 27, 15]
print(solution("TOBEORNOTTOBEORTOBEORNOT")) # [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]
print(solution("ABABABABABABABAB")) # [1, 2, 27, 29, 28, 31, 30]