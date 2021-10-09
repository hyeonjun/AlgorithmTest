"""
조합 공식 : nCm = n! / (n-m)! * m!
"""
import math
n, m = map(int, input().split())
parent = math.factorial(n)
child = (math.factorial(n-m)) * math.factorial(m)
print(parent//child)