def prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def dfs(num):
    if len(num) == n:
        print(num)
        return

    for i in range(10):
        newValue = num+str(i)
        if prime(int(newValue)): # 1자리, 2자리, 3자리, 4자리 소수 확인
            dfs(newValue)

n = int(input())
m = [2, 3, 5, 7]
for x in m:
    dfs(str(x))