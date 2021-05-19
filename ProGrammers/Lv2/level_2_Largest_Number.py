def solution(numbers):
    numbers = list(map(str, numbers))
    numbers = sorted(numbers, reverse=True, key=lambda x : x*(5-len(x)) if len(x) < 4 else x)
    return str(int(''.join(numbers)))

print(solution([6,10,2])) # "6210"
print(solution([3,30,34,5,9])) # "9534330"