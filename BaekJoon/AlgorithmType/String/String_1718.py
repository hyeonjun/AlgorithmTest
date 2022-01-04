A = input()
B = input()
answer = ''
for i in range(len(A)):
    if A[i] == ' ':
        answer += ' '
    else:
        answer += chr( (ord(A[i]) - ord(B[i%len(B)]) - 1) % 26 + ord('a') )
print(answer)