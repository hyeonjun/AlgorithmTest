def solution(a, b):
    star = ""
    for i in range(b):
        star+=("*" * a+"\n")
    return star

print(solution(5,3))
print(solution(2,2))

def solution(a, b):
    return ('*' * a + '\n') * b

print(solution(5,3))
print(solution(2,2))
