def MySolution(A): # 55% 시간복잡도에서 걸림 O(n^2)
    if len(A) == 1:
        return 0
    count = 0
    for i in range(len(A)-1):
        right = {}
        left = {}
        for r in A[:i+1]:
            if r not in right.keys():
                right[r] = 1
            else:
                right[r] += 1
        for l in A[i+1:]:
            if l not in left.keys():
                left[l] = 1
            else:
                left[l] += 1

        rMax = max(right.values())
        lMax = max(left.values())
        rValue = lValue = 0
        if rMax > len(A[:i+1])/2 and lMax > len(A[i+1:])/2:
            for key, value in right.items():
                if rMax == value:
                    rValue = key
            for key, value in left.items():
                if lMax == value:
                    lValue = key
            if rValue == lValue:
                count+=1
    return count
    pass

def solution(A):
    count = 0

    right = {}
    right_len = len(A)
    for i in A:
        if i not in right:
            right[i] = 1
        else:
            right[i] += 1

    left = {}
    left_len = 0
    left_leader = 0
    left_leader_prev = 0
    for i in range(len(A)-1):
        right[A[i]] -= 1
        right_len -= 1

        try:
            left[A[i]] += 1
        except:
            left[A[i]] = 1
        left_len += 1

        if left[A[i]] > left_leader_prev: # value가 높은거
            left_leader = A[i] # left에서 가장 value가 높은 key값
            left_leader_prev = left[A[i]]
        # left의 가장 높은 value가 left의 길이의 절반보다 큰지,
        # left에서 가장 value가 높은 key이 right에서 몇 개인지보고 그 값이 right의 길이의 절반보다 큰지
        if (left_leader_prev > left_len//2) and (right[left_leader] > right_len//2):
            count += 1

    return count


print(solution([4,3,4,4,4,2]))

# 3 4 4 2
# 3 | 4 4 2
# 3 4 x
# 3 4 | 4 2
# x
# 3 4 4 | 2
# 4 2 x
