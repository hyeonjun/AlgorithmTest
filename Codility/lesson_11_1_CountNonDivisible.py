def solution(A):
    N = len(A)
    element = [0] * (2*N+1)
    for data in A:
        element[data] += 1

    result = [0] * N
    saved = [-1] * (2*N+1)
    for i in range(N):
        current = A[i]
        if saved[current] != -1:
            result[i] = saved[current]
        else:
            count = 0
            for j in range(1, int(current**0.5)+1):
                if current % j == 0:
                    # 나눠지는 갯수 구함, 3이 두개 있으니 두개가 한번에 계산됨
                    count += element[j]
                    if j*j != current:
                        count+=element[current//j]
            result[i] = N - count
            saved[current] = result[i]
    return result

    # [0, 1, 1, 2, 0, 0, 1, 0, 0, 0, 0]

    # if len(A) == 1: # O(N**2)
    #     return [0]
    # result = [0] * N
    # for i in A:
    #     count = 0
    #     for j in A:
    #         if i % j != 0:
    #             count+=1
    #     result.append(count)
    # return result


print(solution([3,1,2,3,6,4]))

