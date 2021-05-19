def solution(clothes):
    answer = 1
    check = {}
    for i in clothes:
        if i[1] in check:
            check[i[1]] += 1
        else:
            check[i[1]] = 1
    for i in check:
        answer *= (check[i]+1)
    return answer-1

# 5
print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))

# 3
print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))