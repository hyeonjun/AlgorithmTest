def solution(n):
    binary = bin(n).count('1')
    while True:
        n+=1
        if binary == bin(n).count('1'):
            return n

print(solution(78))
print(solution(15))