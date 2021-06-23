def solution(A, B):
    answer = 0
    B.sort(reverse=True)
    A.sort(reverse=True)
    for a in A:
        scoreB = a
        for b in B:
            if a < b:
                scoreB = b
            else:
                break
        if scoreB == a:
            continue
        else:
            B.remove(scoreB)
            answer += 1

    return answer

print(solution([5,1,3,7],[2,2,6,8]))
print(solution([2,2,2,2],[1,1,1,1]))