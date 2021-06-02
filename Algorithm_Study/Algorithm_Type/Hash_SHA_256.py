def solution(data):
    from hashlib import sha256
    return sha256(data.encode()).hexdigest() 

print(solution("Baekjoon"))