def solution(A, B):
    def gcd(x, y): # 최대 공약수
        while y:
            x, y = y, x%y
        return x

    def prime(x, y):
        while x != 1:
            value = gcd(x,y)
            if value == 1:
                break
            x //= value
        return True if x == 1 else False

    result = 0
    for a, b in zip(A, B):
        value = gcd(a,b)
        if prime(a, value) and prime(b, value):
            result += 1
    return result
print(solution([15,10,3],[75,30,5]))