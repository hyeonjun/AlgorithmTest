# 이름 궁합
def solution(n, m, N, M):
    alp = [3,2,1,2,4,3,1,3,1,1,3,1,3,2,1,2,2,2,1,2,1,1,1,2,2,1]
    NM = ""
    length = min(n, m)

    for i in range(length):
        NM += N[i]+M[i]
    NM += N[length:] + M[length:]

    score = [alp[ord(s)-ord('A')] for s in NM]

    for i in range(n+m-2):
        for j in range(n+m-1-i):
            score[j] = (score[j]+score[j+1]) % 10
    return "{0}%".format(score[0] * 10 + score[1])

print(solution(8,14,"LEESIYUN", "MIYAWAKISAKURA")) # 27%
print(solution(2,2, "AB","CD")) # 77%
print(solution(3,2, "BOJ", "IN")) # 1%