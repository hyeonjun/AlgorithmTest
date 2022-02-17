from collections import Counter
r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]


answer = 0

def RC():
    maxlen = 0
    for i in range(len(A)):
        cnt = Counter(A[i])
        del cnt[0] # 0은 삭제
        cnt = sorted(cnt.items(), key=lambda x: (x[1], x[0])) # 빈도수, 수
        A[i] = []
        for c, n in cnt:
            A[i].extend([c, n])
        A[i] = A[i][:100]
        maxlen = max(maxlen, len(A[i]))

    for i in range(len(A)):
        if len(A[i]) < maxlen:
            A[i] += [0] * (maxlen - len(A[i]))

while True:
    if r-1 < len(A) and c-1 < len(A[0]) and A[r-1][c-1] == k:
        break
    if len(A) >= len(A[0]): # R연산
        RC()
    else:
        A = list(zip(*A)) # 트랜스포즈
        RC()
        A = list(zip(*A)) # 원상복귀

    answer += 1
    if answer > 100:
        answer = -1
        break
print(answer)
