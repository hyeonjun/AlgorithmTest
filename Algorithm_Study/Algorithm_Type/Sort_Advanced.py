# 오름차순 정렬
def solution(array):
    return sorted(array)

print(solution([5,4,3,2,1]))

def solution(array): # 병합 정렬
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = solution(array[:mid])
    right = solution(array[mid:])
    i, j, k = 0,0,0
    while i<len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j+= 1
        k += 1
    if i == len(left):
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
    elif j== len(right):
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
    return array
print(solution([5,4,3,2,1]))

# ===========================================================================

# 오름차순 정렬 후, K번째에 있는 수
def solution(K, array):
    return sorted(array)[K-1]

print(solution(2, [4,1,2,3,5]))

# ===========================================================================

