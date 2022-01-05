answer = ''
for s in input():
    if s.isupper():
        answer += s.lower()
    else:
        answer += s.upper()
print(answer)