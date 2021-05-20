def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length
    while bridge:
        answer += 1
        bridge.pop(0)
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)
    return answer

print(solution(2, 10, [7,4,5,6])) # 8
print(solution(100, 100, [10]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))
