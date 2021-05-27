def Sequential_Search_1(data, n):
    return True if n in data else False

def Sequential_Search_2(data, n):
    for i in range(len(data)):
        if n == data[i]:
            return i
    return -1

from random import randint
rand_data = [0] * 10
for i in range(10):
    rand_data[i] = randint(1,100)
print(rand_data)
print(Sequential_Search_1(rand_data, 77))
print(Sequential_Search_2(rand_data, 77))


