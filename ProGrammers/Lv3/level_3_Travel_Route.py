def solution(tickets):
    routes = {}
    answer = []
    # for t in tickets:
    #     routes[t[0]] = routes.get(t[0], []) + [t[1]]

    for t in tickets:
        if t[0] in routes:
            routes[t[0]] += [t[1]]
        else:
            routes[t[0]] = [t[1]]

    for r in routes:
        routes[r].sort(reverse=True)
    stack = ["ICN"]

    while stack:
        data = stack[-1]
        if data in routes and routes[data]:
            stack.append(routes[data].pop())
        else:
            answer.append(stack.pop())

    return answer[::-1]

# ["ICN", "JFK", "HND", "IAD"]
print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
# ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))