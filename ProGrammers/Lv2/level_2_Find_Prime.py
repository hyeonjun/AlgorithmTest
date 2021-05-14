def solution(numbers):
    answer = []
    def isPrime(n):
        import math
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1): # math.sqrt(n) => n ** 0.5
            if n % i == 0:
                return False
        return True

    from itertools import permutations
    for i in range(1, len(numbers) + 1):
        makeN = list(set(map("".join, permutations(numbers, i))))
        for j in makeN:
            if isPrime(int(j)):
                answer.append(int(j))
    return len(set(answer))

print(solution("17"))
print(solution("011"))