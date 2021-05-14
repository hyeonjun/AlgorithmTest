def quick_sort(data): # O(n log n) 최악 : O(N^2)
    if len(data) <=1:
        return data
    pivot = data[0]

    left = [i for i in data[1:] if pivot > i]
    right = [i for i in data[1:] if pivot < i]

    # left, right = [], []
    # for i in range(1, len(data)):
    #     left.append(data[i]) if pivot > data[i] else right.append(data[i])

    return quick_sort(left) + [pivot] + quick_sort(right)
import random
data = random.sample(range(100), 10)
print(data)
print(quick_sort(data))