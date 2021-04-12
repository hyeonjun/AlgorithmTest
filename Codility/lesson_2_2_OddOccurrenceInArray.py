def solution(A):
    dict = {}
    for i in A:
        if i in dict: # or -> if dict.get(i):
            dict[i] += 1
        else:
            dict[i] = 1
    print(dict)
    for i in dict:
        if(dict[i]%2 != 0):
            return i


print(solution([9, 3, 9, 3, 9, 7, 9]))
print(solution([42]))


dict = {}
dict[1] = 0
print(dict) # {1:0}