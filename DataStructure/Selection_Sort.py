def selection_sort(data):
    for i in range(len(data)-1):
        minV = data.index(min(data[i:]))
        data[i], data[minV] = data[minV], data[i]
    return data

import random
data_list = random.sample(range(100), 10)
print(selection_sort(data_list))
