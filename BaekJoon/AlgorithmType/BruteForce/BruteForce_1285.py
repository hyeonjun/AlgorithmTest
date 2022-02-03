"""
ex) n = 3
각 행은
    0 0 0
    0 0 1
    0 1 0
    1 0 0
    0 1 1
    1 1 0
    1 0 1
    1 1 1
    => 경우의 수 = 2^3 = 1 << 3
"""
n = int(input())
arr = [list(input()) for _ in range(n)]
answer = n ** 2 # 최대: 전체가 뒷면

for case in range(1 << n): # 바꿀 경우의 수
    cnt = 0 # min(H, T): T가 최소이면 T, H가 최소이면 H를 뒤집어서 T로 생각
    for i in range(n): # 열
        T = 0 # T 개수
        for j in range(n): # 행
            tmp = arr[j][i]
            # 해당 case로 바꿔버리기
            if case & (1 << j): # 행 뒤집기
                if tmp == 'T':
                    tmp = 'H'
                else:
                    tmp = 'T'
            if tmp == 'T':
                T += 1
        # 이 case로 바꿨을 때 적은 T 개수 저장
        # 즉, H가 적으면 안바꿈, T가 적으면 바꿈
        cnt += min(n-T, T) # min(H, T)
    answer = min(answer, cnt)
print(answer)