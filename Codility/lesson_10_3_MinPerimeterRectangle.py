def solution(N):
    side_list = []
    if N == 1:
        return 4
    for i in range(1,N):
        if i*i > N:
            break
        if i*i == N:
            return (i+i)*2
        if N % i == 0:
            side_list.append(i)
            side_list.append(N//i)
    side_list.sort()
    len_side = len(side_list)//2
    return (side_list[len_side-1]+side_list[len_side])*2

# print(solution(16))
# print(solution(30))
print(solution(1))

