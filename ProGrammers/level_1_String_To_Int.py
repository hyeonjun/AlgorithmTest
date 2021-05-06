def solution(s):
    return int(s)

print("-1234")
print("1234")

def solution(s):
    answer = 0
    number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i, n in enumerate(s[::-1]):
        if n == '-':
            answer *= -1
        else:
            answer += number[n] * (10 ** i)
    return answer

print("-1234")
print("1234")