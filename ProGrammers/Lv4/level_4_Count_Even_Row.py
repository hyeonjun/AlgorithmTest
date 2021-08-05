from collections import defaultdict
# comb(n, k) : 반복과 순서없이 n개의 항목에서 k개의 항목을 선택하는 방법의 수
from math import comb # k <= n, n! / (k! * (n-k)!) || k > n, 0
from functools import lru_cache

def solution(a):
    @lru_cache(maxsize=None)  # 데코레이터를 사용하여 함수의 반환값들을 메모이제이션할 수 있음
    def C(n, k):
        return comb(n, k)
    rows = len(a)
    one_cnt = [sum(ones) for ones in zip(*a)] # 각열 1의 갯수, [2, 4, 2]
    # dp[i][j] = k -> i열까지 계산했을 때 j개의 짝수행을 가지는 b의 개수는 k
    DP = defaultdict(int, {rows-one_cnt[0]: comb(rows, one_cnt[0])})
    # 1열까지 계산한 DP, {2 : 6}
    print(DP)
    for ones in one_cnt[1:]: # DP[2][j] 부터 계산
        next_DP = defaultdict(int)
        for even_rows in DP:
            odd_rows = rows-even_rows # 홀수행 개수는 rows-짝수행
            # add_one의 최소값 : 1을 더할 짝수행의 최소개수, max(0, ones-odd_rows)
            # add_one의 최대값 : 1을 더할 짝수행의 최대개수, min(ones, even_rows)
            for add_one in range(max(0,ones-odd_rows), min(ones,even_rows)+1):
                # 기존 짝수행 개수에서 새로 만들어지는 짝수행 개수
                # dp[짝수행개수 - 추가할 1의 개수 + 현재열의 1의 개수 - 추가할 1의 개수]
                # = 짝수행 개수의 경우의 수 * 1이 더해질 짝수행 개수를 고르는 경우의 수 * 1이 더해질 홀수행 개수를 고르는 경우의 수
                next_DP[even_rows+ones-2*add_one] += DP[even_rows] * C(even_rows, add_one) * C(odd_rows, ones-add_one) % (10**7+19)
        DP = next_DP
        print(DP)
    return DP[rows]

print(solution([[0,1,0],[1,1,1],[1,1,0],[0,1,1]])) # 6
print(solution([[1,0,0],[1,0,0]])) # 0
print(solution([[1,0,0,1,1],[0,0,0,0,0],[1,1,0,0,0],[0,0,0,0,1]])) # 72