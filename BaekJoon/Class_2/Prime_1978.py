n = int(input())
num = list(map(int, input().split()))
cnt = 0

def prime(d):
    if d < 2:
        return False
    if d == 2:
        return True
    for i in range(2, int(d**0.5)+1):
        if d % i == 0:
            return False
    return True

for i in num:
    if prime(i):
        cnt += 1
print(cnt)