"""
 i          0  1  2  3  4  5
 arr[i]     0  1  2  3  1  2
 ps[i]      0  1  3  6  7  9
 ps[i] % m  0  1  0  0  1  0

구간합의 나머지 개수를 배열에 넣음(해당 인덱스가 나머지를 의미)
    => hashmap = [3, 2]

(ps[j] - ps[i]) % m = 0 일 때,
 ps[j] % m = ps[i] % m

1 - 1 => (1, 4)
0 - 0 => (2, 3), (2, 5), (3, 5), (0, 2), (0, 3), (0, 5)

ps[i]의 개수 중 2개를 고르면 그 사이의 합이 나머지 0이 된다.
    => ps[i]C2 => (ps[i] * (ps[i] - 1)) / 2
"""
import sys
input=sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))

S = 0
hashmap = [0 for _ in range(int(1001))]
for i in range(1, n+1):
    S = (S + arr[i-1]) % m
    hashmap[S] += 1

answer = hashmap[0] # 0은 이미 나머지가 0이기 때문
for i in range(m):
    answer += (hashmap[i] * (hashmap[i] - 1)) // 2
print(answer)