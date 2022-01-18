S = input()
T = list(input())
answer = 0
while T:
    t = T.pop()
    if t == 'B':
        T = T[::-1]
    if S == ''.join(T):
        answer = 1
        break
print(answer)