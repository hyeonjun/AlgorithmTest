# 두 번 이상 나오는 부분 문자열 중 가장 긴 것.
def make_table(pattern): #get Pi
    pi = [0 for _ in range(len(pattern))]
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j-1]
        if pattern[i] == pattern[j]:
            j += 1
            pi[i] = j
    return max(pi)

S = input()
answer = 0
for i in range(len(S)):
    pattern = S[i:len(S)]
    print(pattern)
    answer = max(answer, make_table(pattern))
print(answer)