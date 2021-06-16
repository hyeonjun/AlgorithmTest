def solution(routes): # O(N^2)
    answer = 0
    routes.sort(key=lambda x: x[1])
    check = [0] * len(routes)

    for i in range(len(routes)):
        if check[i] == 0:
            camera = routes[i][1]
            answer += 1
            check[i] = 1
        for j in range(i + 1, len(routes)):
            if routes[j][0] <= camera <= routes[j][1] and check[j] == 0:
                check[j] = 1

    return answer

print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]])) # 2

def solution(routes): # O(N)
    answer = 0
    routes.sort(key=lambda x:x[1])
    camera = min(routes, key=lambda x:x[0])[0] -1
    for route in routes:
        if camera < route[0]:
            answer += 1
            camera = route[1]
    return answer

print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]])) # 2