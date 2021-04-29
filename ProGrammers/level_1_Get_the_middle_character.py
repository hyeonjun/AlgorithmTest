def solution(s):
    N = len(s)
    return s[(N-1)//2] if N%2 != 0 else s[N//2-1:N//2+1]

print(solution("abcde"))
print(solution("qwer"))