N, m, M, T, R = map(int, input().split())
answer = cnt = 0
m_ = m
if m+T > M:
    print(-1)
else:
    while cnt < N:
        if m_+T <= M: # 운동
            cnt += 1
            m_ += T
        else: # 휴식
            m_ = max(m_-R, m)
        answer += 1
    print(answer)