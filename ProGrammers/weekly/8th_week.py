def solution(sizes):
    maxX, maxY = 0, 0
    for i in sizes:
        if max(i) == i[1]:
            i[0],i[1] = i[1], i[0]
        maxX = max(maxX, i[0])
        maxY = max(maxY, i[1])
    return maxX * maxY

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]])) # 4000
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]])) # 120
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]])) # 133


def solution(sizes):
    return max(max(i) for i in sizes) * max(min(i) for i in sizes)

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]])) # 4000
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]])) # 120
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]])) # 133