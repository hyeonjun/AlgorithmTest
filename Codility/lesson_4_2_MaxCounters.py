def MySolution(N, A): # 77%
    count = [0] * N
    next_max = 0
    for i in A:
        if i > N:
            count = [next_max] * N
        else:
            count[i-1] = current_value = count[i-1]+1
            next_max = max(current_value, next_max)
    return count

print(MySolution(5, [3,4,4,6,1,4,4]))

def solution(N, A): # 100%
    count = [0] * N
    next_max = max_counter = 0
    for i in A:
        try:
            current_counter = count[i-1] = max(count[i-1]+1, max_counter+1)
            next_max = max(current_counter, next_max)
        except:
            max_counter = next_max
    return [c if c > max_counter else max_counter for c in count]

print(solution(5, [3,4,4,6,1,4,4]))

