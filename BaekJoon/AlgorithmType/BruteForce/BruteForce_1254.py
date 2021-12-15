s = input()
answer = len(s)
for i in range(len(s)):
    if s[i:] == s[i:][::-1]:
        answer += i
        break
print(answer)