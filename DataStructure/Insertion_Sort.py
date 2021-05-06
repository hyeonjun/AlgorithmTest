def insertion_sort(data):
    for i in range(1, len(data)):
        value = data[i]
        for j in range(i):
            if data[j] > value:
                del data[i]
                data.insert(j, value)
                break
    return data

import random
data_list = random.sample(range(100), 10)
print(insertion_sort(data_list))

def insertion_sort(data):
    for i in range(len(data)-1):
        for j in range(i+1, 0, -1):
            if data[j] < data[j-1]:
                data[j], data[j-1] = data[j-1], data[j]
            else:
                break
    return data

print(insertion_sort(data_list))

