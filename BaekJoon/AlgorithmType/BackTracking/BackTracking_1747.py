def prime(x):
    if x == 1:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i ==0:
            return False
    return True
n = int(input())
answer = 0
while True:
    if prime(n) and str(n) == str(n)[::-1]:
        answer = n
        break
    n += 1
print(answer)