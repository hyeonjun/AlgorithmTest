def solution(n, array):
    return sorted(array, key=lambda x:x[0])

print(solution(3, [[21,"Junkyu"],[21, "Dohyun"],[20, "Sunyoung"]]))

# ============================================================================

def solution(coordinates):
    return sorted(coordinates)

# [[1, -1], [1, 1], [2, 2], [3, 3], [3, 4]]
print(solution([[3,4],[1,1],[1,-1],[2,2],[3,3]]))

# ============================================================================

def solution(array):
    return sorted(array)

print(solution([5,2,3,1,4,2,3,5,1,7]))

def solution(n, array):
    number = [0] * 10001

    for i in array:
        number[i] += 1
    answer = []
    for i in range(len(number)):
        if number[i] != 0:
            for j in range(number[i]):
                answer.append(i)
    return answer
    pass

print(solution(10, [5,2,3,1,4,2,3,5,1,7]))

# ============================================================================

def solution(data):
    return sorted(data)
print(solution([5,5,2,3,4,1]))

# 선택 알고리즘
def solution(data):
    for i in range(len(data)):
        min_index = i
        for j in range(i+1, len(data)):
            if data[min_index] > data[j]:
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]
    return data
print(solution([5,5,2,3,4,1]))

# ============================================================================

def solution(data):
    data = sorted(list(str(data)), reverse=True)
    return int(''.join(data))
print(solution(2143))

def solution(data):
    data = str(data)
    answer = []
    for i in range(9, -1, -1):
        for j in data:
            if int(j) == i:
                answer.append(j)
    return int(''.join(answer))

print(solution(2143))

