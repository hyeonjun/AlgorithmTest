def bubblesort(data):
    for i in range(len(data) -1):
        swap = False
        for j in range(len(data) - i - 1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                swap = True
        if swap == False:
            break
    return data

import random
data_list = random.sample(range(100), 50)
print(bubblesort(data_list))

data_list = random.sample(range(100), 10)
for i in range(50):
    data_list = random.sample(range(100), 50)
    print(bubblesort(data_list))