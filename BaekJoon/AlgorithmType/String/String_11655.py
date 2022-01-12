string = input()
answer = ''
for s in string:
    if s.isupper():
        answer += chr((ord(s) - ord('A') + 13) % 26 + ord('A'))
    elif s.islower():
        answer += chr((ord(s) - ord('a') + 13) % 26 + ord('a'))
    else:
        answer += s
print(answer)