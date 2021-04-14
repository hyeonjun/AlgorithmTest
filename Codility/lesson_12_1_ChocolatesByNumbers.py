# def solution(N, M):
#     result = [0] * N
#     idx = 0
#     while True:
#         if result[(idx+M)%N] != 1:
#             result[(idx + M) % N] = 1
#             idx=(idx + M) % N
#         else:
#             break
#     count = 0
#     for i in result:
#         if i == 1:
#             count+=1
#     return count
#
#
# print(solution(10, 4))

def solution(N,M): # 최대공약수
    a = N
    while M:
        N, M = M, N%M
    return a//N

print(solution(10, 4))















