def solution(strings, n):
    return sorted(sorted(strings), key=lambda x : x[n])

print(solution(["sun","bed","car"], 1))
print(solution(["abce","abcd","cdx"], 1))

# sorted에는 key