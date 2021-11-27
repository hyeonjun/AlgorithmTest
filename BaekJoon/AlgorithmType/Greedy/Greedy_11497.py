"""
인덱스 차가 1로 두고 계산하면 첫번째 통나무와 마지막 통나무의 차가 커진다.
인덱스 차를 2로 두면 최소값으로 구할 수 있다.
"""
for _ in range(int(input())):
    n = int(input())
    log = sorted(map(int, input().split()))
    answer = 0
    for i in range(n-2):
        answer = max(answer, abs(log[i]-log[i+2]))
    print(answer)