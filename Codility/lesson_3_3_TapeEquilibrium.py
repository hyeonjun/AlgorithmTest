# N개의 정수로 구성된 비어있지 않은 배열 A
# 배열 A를 두 개로 분할
# 분할 했을 때 두개의 차이값이 최소인것을 반환
# 차이값은 절대값이다
# 즉, 분할은 배열의 길이-1만큼 할 수있다

# def MySolution(A): # 시간복잡도 O(N*N)
#     result = []
#     P = len(A)
#     for i in range(1, P):
#         if i == 1:
#             result.append(abs(A[0]-sum(A[1:])))
#         else:
#             result.append(abs(sum(A[0:i])-sum(A[i:]))) # sum이 많아서 시간복잡도가 증가
#     return min(result)
#
# print(MySolution([3,1,2,4,3])) # 53%

def SideSolution(A): # 시간복잡도 O(N)
    if len(A) == 2:
        return abs(A[0] - A[1])
    result = []
    tmp1 = 0
    tmp2 = sum(A) # 0
    print(tmp2)
    for i in range(len(A)-1):
        tmp1 += A[i] # 0에서 시작하므로 더해줌
        tmp2 -= A[i] # tmp2는 A배열의 전체 합이기때문에 넘어가면서 빼야함
        result.append(abs(tmp1 - tmp2))
    print(result)
    return min(result)
print(SideSolution([-10, -20, -30, -40, 100])) # 100%
