def prime(n):
    if n == 1:
        return True
    for i in range(2, int(n ** 0.5) +1):
        if n % i == 0:
            return False
    return True

A = input()
answer = 0
for a in A:
    if a.isupper():
        answer += ord(a) - ord('A') + 27
    else:
        answer += ord(a) - ord('a') + 1
if prime(answer):
    print('It is a prime word.')
else:
    print('It is not a prime word.')
