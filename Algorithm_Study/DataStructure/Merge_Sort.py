def Merge_Sort(data):
    def merge(left, right):
        merged = []
        left_idx, right_idx = 0, 0

        # case1 : left/right 아직 남아있을 때
        while len(left) > left_idx and len(right) > right_idx:
            if left[left_idx] > right[right_idx]:
                merged.append(right[right_idx])
                right_idx+=1
            else:
                merged.append(left[left_idx])
                left_idx+=1

        # case2 : left만 남아있을 때
        while len(left) > left_idx:
            merged.append(left[left_idx])
            left_idx += 1

        # case3 : right만 남아있을때
        while len(right) > right_idx:
            merged.append(right[right_idx])
            right_idx += 1
        return merged

    def split(data):
        if len(data) <= 1:
            return data
        left = split(data[:len(data)//2])
        right = split(data[len(data)//2:])
        return merge(left, right)

    return split(data)

import random
data = random.sample(range(100), 10)
print(data)
print(Merge_Sort(data))
# 재귀용법
# 리스트를 절반씩 잘게 자름
# 각 부분을 합병하면서 정렬
