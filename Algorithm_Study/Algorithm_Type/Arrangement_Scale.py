def solution(scale):
    descending = sorted(scale, reverse=True)
    ascending = sorted(scale, reverse=False)
    return "ascending" if ascending == scale else "descending" if descending == scale else "mixed"

print(solution([1,2,3,4,5,6,7,8]))
print(solution([8,7,6,5,4,3,2,1]))
print(solution([8,1,7,2,6,3,5,4]))

def solution(scale):
    ascending = True
    descending = True
    for i in range(1, len(scale)):
        if scale[i] > scale[i-1]:
            descending =  False
        elif scale[i] < scale[i-1]:
            ascending = False
    return "ascending" if ascending else "descending" if descending else "mixed"

print(solution([1,2,3,4,5,6,7,8]))
print(solution([8,7,6,5,4,3,2,1]))
print(solution([8,1,7,2,6,3,5,4]))