def solution(s):
    tmp = [int(i) for i in s.split(' ')]
    return str(min(tmp))+ " "+ str(max(tmp))

print(solution("1 2 3 4"))
print(solution("-1 -2 -3 -4"))
print(solution("-1 -1"))