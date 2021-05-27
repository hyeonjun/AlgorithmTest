# recursive
def fibo_recursive(num):
    return num if num <= 1 else fibo_recursive(num-1) + fibo_recursive(num-2)

print(fibo_recursive(10))

# Dynamic
def fibo_dp(num):
    cache = [0, 1] + [0] * (num-1)
    for i in range(2, num+1):
        cache[i] = cache[i-1] + cache[i-2]
    return cache[num]

print(fibo_dp(10))