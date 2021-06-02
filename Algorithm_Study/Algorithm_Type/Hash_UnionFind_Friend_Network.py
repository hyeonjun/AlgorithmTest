def solution(N, data):
    parent = {}
    num = {}
    answer = []
    def find(x):
        if x != parent[x]:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        x = find(x)
        y = find(y)
        if x != y:
            parent[y] = x
            num[x] += num[y]

    for i in data:
        if i[0] not in parent:
            parent[i[0]] = i[0]
            num[i[0]] = 1
        if i[1] not in parent:
            parent[i[1]] = i[1]
            num[i[1]] = 1
        union(i[0], i[1])
        answer.append(num[find(i[0])])
    return answer


print(solution(3, [["Fred", "Barney"], ["Barney", "Betty"], ["Betty", "Wilma"]]))
print(solution(3, [["Fred", "Barney"], ["Betty", "Wilma"], ["Barney", "Betty"]]))