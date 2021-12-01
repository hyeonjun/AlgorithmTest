"""
~k + 1 = -k
k = k - (k & -k)

K = K - (K & ((~k)+1))
    K - (K & - K)
"""
n = int(input())
binary = input()
print(binary.count("1"))
