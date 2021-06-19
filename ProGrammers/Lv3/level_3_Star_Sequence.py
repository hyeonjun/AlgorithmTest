def solution(a):
    from collections import Counter
    elements = Counter(a)
    answer = -1

    for k in elements.keys(): # Counter에 들어온 순서대로 출력함
        if elements[k] <= answer:
            continue
        length = 0
        idx = 0
        while idx < len(a) - 1:
            if (a[idx] == k and a[idx + 1] != k) or a[idx] == a[idx + 1]:
                idx += 1
                continue
            length += 1
            idx += 2
        answer = max(answer, length)

    return answer * 2 if answer != -1 else 0

print(solution([0])) # 0
print(solution([5,2,3,3,5,3])) # 4
print(solution([0,3,3,0,7,2,0,2,2,0])) # 8
