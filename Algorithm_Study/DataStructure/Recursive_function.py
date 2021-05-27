def factorial(x): # O(N)의 시간 복잡도 || 재귀함수는 내부적으로 스택처럼 관리된다
    return x * factorial(x - 1) if x > 1 else x

print(factorial(4))

def factorial(x):
    return x if x<=1 else  x * factorial(x-1)

print(factorial(4))

print("=====================================================================")

import random
data = random.sample(range(100), 10)

def sum_list(x):
    return x[0] if len(x) == 1 else x[-1] + sum_list(x[0:-1])
print(sum_list(data))

def sum_list(x):
    return x[0] if len(x) == 1 else x[0] + sum_list(x[1:])
print(sum_list(data))

def sum_list(x):
    return sum(x)
print(sum_list(data))

print("=====================================================================")

def Palindrome(data):
    if len(data) <= 1:
        return True
    return Palindrome(data[1:-1]) if data[0] == data[-1] else False

print(Palindrome("data"))
print(Palindrome("level"))

def Palindrome(data):
    return data == data[::-1]

print(Palindrome("data"))
print(Palindrome("level"))

print("=====================================================================")

def recursive_1(n):
    # print(n)
    if n == 1:
        return n
    return recursive_1(3 * n + 1) if n % 2 == 1 else recursive_1(n // 2)

print(recursive_1(3))

print("=====================================================================")

def recursive_2(n):
    data = [0, 1, 2, 4]
    return data[n] if n in [1,2,3] else recursive_2(n - 1) + recursive_2(n - 2) + recursive_2(n - 3)

print(recursive_2(5))