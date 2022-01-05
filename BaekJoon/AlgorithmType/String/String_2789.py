A = input()
B = 'CAMBRIDGE'
answer = ''
for a in A:
    if a in B:
        continue
    answer += a
print(answer)