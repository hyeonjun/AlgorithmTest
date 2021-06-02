def solution(n):
    ans = 0
    while n > 0:
        q, r = divmod(n, 2)
        n = q
        if r != 0:
            ans += 1

    # N = 5 0 -> 1(점프 1) -> 2(순간이동) -> 4(순간이동) -> 5(점프 1)
    # N = 6 0 -> 1(점프 1) -> 2(순간이동) -> 4(순간이동) -> 6(점프 2)
    #            1(점프 1) -> 2(순간) -> 3(점프 1) -> 6 순간이동
    # 2 4 8 16 2제곱
    # 3 6 12
    # N = 5000 -> 1(점프 1) -> 2(순간이동) -> 4 8 16 32 64 128 256 512 1024 2048 4096 -> 5000(점프 4)

    return ans

print(solution(6)) # 2
print(solution(5)) # 2
print(solution(5000)) # 5

def solution(n):
    return bin(n).count('1')

print(solution(6)) # 2
print(solution(5)) # 2
print(solution(5000)) # 5